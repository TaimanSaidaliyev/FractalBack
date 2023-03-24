from rest_framework import serializers, generics
from projectManagement.models import *
from userInformation.serializers import UserProfileOut
from rest_framework_recursive.fields import RecursiveField


class StatusViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'title', 'css_color')
        depth = 1


class PriorityViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = ('id', 'title', 'css_color')


class ProjectInformationByIdSerializer(serializers.ModelSerializer):
    managers = serializers.SerializerMethodField()
    moderators = serializers.SerializerMethodField()
    participants = serializers.SerializerMethodField()


    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'bdate', 'edate', 'created_at', 'updated_at', 'status', 'category',
                  'managers', 'moderators', 'participants', )
        depth = 1

    def get_managers(self, obj):
        managers = obj.managers.all()
        return UserProfileOut(managers, many=True).data

    def get_moderators(self, obj):
        moderators = obj.moderators.all()
        return UserProfileOut(moderators, many=True).data

    def get_participants(self, obj):
        participants = obj.participants.all()
        return UserProfileOut(participants, many=True).data


class ProjectParticipantsSerializer(serializers.ModelSerializer):
    participants = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ('participants', )
        depth = 1

    def get_participants(self, obj):
        participants = obj.participants.all()
        return UserProfileOut(participants, many=True).data


class ProjectStatusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'title')
        depth = 1


class ProjectPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = ('id', 'title')
        depth = 1


class TasksListByProjectSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)
    executor = UserProfileOut()
    co_executor = serializers.SerializerMethodField()
    project = ProjectInformationByIdSerializer()

    class Meta:
        model = Tasks
        fields = ('id', 'title', 'project', 'progress', 'is_completed', 'bdate', 'edate', 'tdate',
                  'lft', 'rght', 'tree_id', 'level', 'priority', 'parent', 'status', 'executor', 'co_executor',
                  'children')
        depth = 1

    def to_representation(self, instance):
        task = super().to_representation(instance)
        task['executor'] = UserProfileOut(instance.executor).data
        return task

    def get_co_executor(self, obj):
        co_executor = obj.co_executor.all()
        return UserProfileOut(co_executor, many=True).data


class TasksListShortByProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'level',)
        depth = 1


class TaskAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('__all__')


class ProjectShortInformation(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title')


class TaskDetailShortByIdSerializer(serializers.ModelSerializer):
    project = ProjectShortInformation()

    class Meta:
        model = Tasks
        fields = ('id', 'title', 'project')
        depth = 2


class TaskDetailByIdSerializer(serializers.ModelSerializer):
    executor = UserProfileOut()
    author = UserProfileOut()
    co_executor = serializers.SerializerMethodField()
    viewers = serializers.SerializerMethodField()
    project = ProjectShortInformation()
    status = StatusViewSerializer()
    priority = PriorityViewSerializer()
    related_tasks = serializers.SerializerMethodField()

    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'progress', 'is_completed', 'bdate', 'tdate', 'edate',
                  'created_at', 'updated_at', 'estimated_time', 'project', 'parent', 'priority', 'status',
                  'author', 'executor', 'co_executor', 'viewers', 'related_tasks')
        depth = 2

    def get_co_executor(self, obj):
        co_executor = obj.co_executor.all()
        return UserProfileOut(co_executor, many=True).data

    def get_related_tasks(self, obj):
        related_tasks = obj.related_tasks.all()
        return TaskDetailShortByIdSerializer(related_tasks, many=True).data

    def get_viewers(self, obj):
        viewers = obj.viewers.all()
        return UserProfileOut(viewers, many=True).data


class TimeTrackingSerializer(serializers.ModelSerializer):
    author = UserProfileOut()

    class Meta:
        model = TimeTracking
        fields = ('id', 'description', 'track_date', 'spent_time', 'author')
        depth = 2

    def to_representation(self, instance):
        author = super().to_representation(instance)
        author['author'] = UserProfileOut(instance.author).data
        return author


class TimeTrackingPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeTracking
        fields = ('id', 'description', 'track_date', 'spent_time')
        depth = 2


class TaskHierarchyById(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()

    def to_representation(self, instance):
        representation = {
            'id': instance.id,
            'title': instance.title
        }

        return representation
