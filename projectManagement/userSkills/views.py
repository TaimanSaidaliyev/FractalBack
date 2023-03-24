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
        is_access = ProjectPositionUsers.objects.get(user=request.user)
        return Response(
            ProjectPositionByUserQuestions(is_access, many=False).data
        )