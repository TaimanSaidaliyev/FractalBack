from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from projectManagement.userSkills.serializers import *


class UserAccess(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        is_access = ProjectPositionUsers.objects.get(user=request.user)
        return Response(
            ProjectPositionUsersStatus(is_access, many=False).data
        )


class TestQuestions(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        list = ProjectPositionUsers.objects.get(user=request.user)
        return Response(
            ProjectPositionByUserQuestions(list, many=False).data
        )


class TestAllQuestionsList(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, skill_id):
        skill = Skills.objects.get(pk=skill_id)
        list = SkillQuestion.objects.filter(question_skills_no=skill)
        return Response(
            TestAllQuestionsListSerializer(list, many=True).data
        )

    def post(self, request, skill_id):
        serializer = TestAddQuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = serializer.save()
        skill = Skills.objects.get(pk=skill_id)
        skill.questions.add(question)

        return Response({
            'post': serializer.data
        })


class TestQuestion(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        question = SkillQuestion.objects.get(pk=id)
        return Response(
            TestAddQuestionSerializer(question, many=False).data
        )

    def delete(self, request, id):
        question = SkillQuestion.objects.get(pk=id)
        question.delete()
        return Response(
            'Success'
        )


class TestQuestionAnswer(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, id):
        serializer = TestAddAnswerQuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_record = serializer.save()

        question = SkillQuestion.objects.get(pk=id)
        question.answers.add(new_record)

        return Response({
            'post': serializer.data
        })

    def delete(self, request, id):
        answer = SkillQuestionAnswers.objects.get(pk=id)
        answer.delete()
        return Response(
            'Success'
        )


class SkillList(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        list = Skills.objects.all()
        return Response(
            SkillListSerializer(list, many=True).data
        )


class SkillItem(APIView):
    def get(self, request, skill_id):
        skill = Skills.objects.get(pk=skill_id)
        return Response(
            SkillListSerializer(skill, many=False).data
        )

    def delete(self, request, skill_id):
        question = Skills.objects.get(pk=skill_id)
        question.delete()
        return Response(
            'Success'
        )


class SkillItemAdd(APIView):
    def post(self, request, position_id):
        serializer = SkillAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        skill = serializer.save()

        position = ProjectPosition.objects.get(pk=position_id)
        position.skills.add(skill)

        return Response({
            'post': serializer.data
        })


class ProjectPositionList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        list = ProjectPosition.objects.all()
        return Response(
            ProjectPositionListSerializer(list, many=True).data
        )


class ProjectPositionAdd(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, project_id):
        serializer = ProjectPositionListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project = Project.objects.get(pk=project_id)
        position = serializer.save(project=project)

        return Response({
            'post': serializer.data
        })


class ProjectPositionItem(APIView):
    def delete(self, request, position_id):
        position = ProjectPosition.objects.get(pk=position_id)
        position.delete()
        return Response(
            'Success'
        )


class ProjectPositionSkill(APIView):
    def post(self, request, position_id, skill_id):
        position = ProjectPosition.objects.get(pk=position_id)
        skill = Skills.objects.get(pk=skill_id)
        position.skills.add(skill)
        return Response(
            'Success'
        )

    def delete(self, request, position_id, skill_id):
        position = ProjectPosition.objects.get(pk=position_id)
        skill = Skills.objects.get(pk=skill_id)
        position.skills.remove(skill)
        return Response(
            'Success'
        )
