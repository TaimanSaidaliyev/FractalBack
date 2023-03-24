from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer
from django.contrib.auth.models import User
from userInformation.serializers import UserProfileOut


class ProfileInformation(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, pk):
        currentUser = Profile.objects.get(user=self.request.user.pk)
        user = User.objects.get(pk=pk)
        profile = Profile.objects.get(user=pk)
        if (currentUser.company.pk == profile.company.pk):
            return Response(
            {
                'user': UserSerializer(user).data,
                'profile': ProfileSerializer(profile).data
            })
        else:
            return Response(
            {
                'user': [],
                'profile': []
            })


class ProfileInformationForWidgets(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        return Response(
            UserProfileOut(user, many=False).data
        )


class ProfileCurrentUser(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = User.objects.get(pk=self.request.user.pk)
        profile = Profile.objects.get(pk=self.request.user.pk)
        return Response(
        {
            'user': UserSerializer(user).data,
            'profile': ProfileSerializer(profile).data
        })