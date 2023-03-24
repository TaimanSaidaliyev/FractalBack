from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import Response, APIView
from .models import Company
from .serializers import CompanyInformationSerializer
from userInformation.models import Profile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


def userCompany(pk):
    user = Profile.objects.get(pk=pk)
    company_pk = Company.objects.get(pk=user.company.pk)
    return company_pk


class TokenList(APIView):

    def post(self, request):
        token = request.data['api_token']
        user_id = Token.objects.get(key=token).user_id
        user = User.objects.get(pk=user_id)
        return Response({
            'id': user.pk,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'email_verified_at': '2023-01-25T12:13:02.000000Z',
            'created_at': user.date_joined,
            'updated_at': user.last_login,
            'api_token': token
            }
        )


class CompanyInformationByUserId(APIView):

    def get(self, request):
        user = User.objects.get(pk=request.user.pk)
        company = Company.objects.get(pk=user.pk)
        return Response({
            'company': CompanyInformationSerializer(company, many=False).data
        })


class UploadImage(APIView):

    def post(self, request):
        if request.method == 'POST' and request.FILES.get('image'):
            image = request.FILES['image']
            filename = default_storage.get_available_name(image.name)
            path = default_storage.save(filename, ContentFile(image.read()))
            url = default_storage.url(path)
            return Response(request.build_absolute_uri(url))
        else:
            return ('Invalid request method or no image uploaded.')
