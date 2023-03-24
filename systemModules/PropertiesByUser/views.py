from rest_framework.views import Response, APIView
from systemModules.models import PropertiesByUserBool, TypeOfPropertiesByUserBool
from .serializers import PropertyItemPutSerializer, PropertyItemGetSerializer
from rest_framework.permissions import IsAuthenticated
from systemModules.models import Company, Module
from userInformation.models import Profile
from news.models import News


def userCompany(pk):
    user = Profile.objects.get(pk=pk)
    company_pk = Company.objects.get(pk=user.company.pk)
    return company_pk


class PropertyItemPut(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, type_id, module_id, record_id, is_liked=None):
        serializer = PropertyItemPutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        module = Module.objects.get(pk=module_id)
        company = userCompany(request.user.pk)
        type_field = TypeOfPropertiesByUserBool.objects.get(pk=type_id)

        try:
            is_liked = PropertiesByUserBool.objects.get(user=request.user,
                                                        record_id=record_id,
                                                        company=company,
                                                        module=module,
                                                        type=type_field.pk)
        except:
            None

        if (is_liked):

            if(is_liked.isBool):
                is_liked.isBool = False
                is_liked.save()
                return Response({
                    'like': PropertyItemGetSerializer(is_liked, many=False).data
                })
            else:
                is_liked.isBool = True
                is_liked.save()
                return Response({
                    'like': PropertyItemGetSerializer(is_liked, many=False).data
                })
        else:
            serializer.save(user=request.user,
                            record_id=record_id,
                            company=company,
                            type=type_field,
                            module=module,
                            isBool=True
                            )

        return Response({
            'like': PropertyItemGetSerializer(is_liked, many=False).data
        })


class PropertyItemGet(APIView):
    def get(self, request, type_id, module_id, record_id, like=None):
        module = Module.objects.get(pk=module_id)
        company = userCompany(request.user.pk)
        type_field = TypeOfPropertiesByUserBool.objects.get(pk=type_id)
        # Count of property
        try:
            count = PropertiesByUserBool.objects.filter(record_id=record_id,
                                                        module_id=module,
                                                        type=type_field.pk,
                                                        company=company,
                                                        isBool=True).count()
        except:
            count = 0

        # True or False of user property
        try:
            like = PropertiesByUserBool.objects.get(user=request.user,
                                                    record_id=record_id,
                                                    company=company,
                                                    module=module,
                                                    type=type_field.pk)

            return Response({
                'like': PropertyItemGetSerializer(like, many=False).data,
                'count': count
            })
        except:
            return Response({
                'like': {'isBool': False},
                'count': count
            })


