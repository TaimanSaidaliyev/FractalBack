from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from utils.utils import userCompany
from projectManagement.serializers import *
from django.db.models import Sum


def task_parent_hierarchy(task_id):
    task = Tasks.objects.get(pk=task_id)
    parent = task.parent
    task_hierarchy = []
    task_hierarchy.append(task)
    while ((parent is None) == False):
        task = Tasks.objects.get(pk=parent.pk)
        task_hierarchy.append(task)
        parent = task.parent
    task_hierarchy.reverse()
    context = task_hierarchy
    return context


class TaskListByProject(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, project_id):
        project = Project.objects.get(pk=project_id, company=userCompany(self.request.user.pk))
        tasks = Tasks.objects.filter(project=project, company=userCompany(self.request.user.pk),
                                     parent__isnull=True)
        return Response({
            'task_list': TasksListByProjectSerializer(tasks, many=True).data
        })


class ProjectInformationById(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, project_id):
        project = Project.objects.get(pk=project_id, company=userCompany(self.request.user.pk))

        return Response(
            ProjectInformationByIdSerializer(project, many=False).data
        )


class TaskAddByProject(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, project_id):
        project = Project.objects.get(pk=project_id, company=userCompany(self.request.user.pk))
        status = Status.objects.filter(company=userCompany(self.request.user.pk))
        priority = Priority.objects.filter(company=userCompany(self.request.user.pk))
        parent_tasks = Tasks.objects.filter(company=userCompany(self.request.user.pk), project=project)

        return Response({
            'parent_tasks': TasksListShortByProjectSerializers(parent_tasks, many=True).data,
            'participants': ProjectParticipantsSerializer(project, many=False).data,
            'status': ProjectStatusListSerializer(status, many=True).data,
            'priority': ProjectPrioritySerializer(priority, many=True).data
        })

    def post(self, request, project_id):
        project = Project.objects.get(pk=project_id, company=userCompany(self.request.user.pk))
        serializer = TaskAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user, company=userCompany(self.request.user.pk), project=project)
        return Response({
            'post': serializer.data
        })


class TaskDetailById(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, project_id, task_id):
        project = Project.objects.get(pk=project_id, company=userCompany(self.request.user.pk))
        task = Tasks.objects.get(pk=task_id, project=project, company=userCompany(self.request.user.pk))

        return Response({
            'task_detail': TaskDetailByIdSerializer(task, many=False).data,
            'task_hierarchy': TaskHierarchyById(task_parent_hierarchy(task_id), many=True).data
        })

    def put(self, request, project_id, task_id):
        pk = task_id
        if not pk:
            return Response({"error": "Method PUT now allowed"})
        try:
            instance = Tasks.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = TaskAddSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, project_id, task_id):
        project = Project.objects.get(pk=project_id, company=userCompany(self.request.user.pk))
        task = Tasks.objects.get(pk=task_id, project=project, company=userCompany(self.request.user.pk))
        task.delete()

        return Response(
            'Deleted'
        )


class TaskTimeTracking(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, project_id, task_id):
        project = Project.objects.get(pk=project_id, company=userCompany(self.request.user.pk))
        task = Tasks.objects.get(pk=task_id, project_id=project, company=userCompany(self.request.user.pk))
        time_tracking = TimeTracking.objects.filter(task=task).order_by('pk')
        time_tracking_count = time_tracking.aggregate(Sum('spent_time'))['spent_time__sum']
        return Response(
            {
                'time_tracking': TimeTrackingSerializer(time_tracking, many=True).data,
                'spent_time': time_tracking_count
            }

        )

    def post(self, request, project_id, task_id):
        project = Project.objects.get(pk=project_id, company=userCompany(self.request.user.pk))
        task = Tasks.objects.get(pk=task_id, project_id=project, company=userCompany(self.request.user.pk))

        serializer = TimeTrackingPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user,
                        company=userCompany(self.request.user.pk),
                        task=task)
        return Response(
            serializer.data
        )

    def delete(self, request, timetracking_id):
        time_tracking = TimeTracking.objects.get(pk=timetracking_id)
        time_tracking.delete()
        return Response(
            'success'
        )
