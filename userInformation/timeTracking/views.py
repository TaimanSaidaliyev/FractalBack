from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from userInformation.models import StartDay, TimeTrackingProperties
from systemModules.models import Company
from userInformation.models import Profile
import datetime
from time import strftime
from .serializers import TimeTrackingListSerializer, TimeTrackingPropertySerializer


def userCompany(pk):
    user = Profile.objects.get(pk=pk)
    company_pk = Company.objects.get(pk=user.company.pk)
    return company_pk


class TimeTrackingUser(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, status=None):
        current_date = datetime.date.today()
        try:
            track = StartDay.objects.get(user=self.request.user.pk,
                                         company=userCompany(self.request.user.pk),
                                         date=current_date)
        except:
            track = StartDay(user_id=self.request.user.pk, company=userCompany(self.request.user.pk),date=current_date)
            track.save()

        if (track.is_working == False and track.is_ended == False):
            status = 1
        elif (track.is_working == True):
            status = 2
        elif (track.is_ended == True):
            status = 3

        return Response(
            {
                'time_tracking_status': status
            }
        )

    def post(self, request):
        current_date = datetime.date.today()
        track = StartDay.objects.get(user=self.request.user.pk,
                                     company=userCompany(self.request.user.pk),
                                     date=current_date)

        if (track.is_working == False and track.is_ended == False):
            track.is_working = True
            track.start_time = strftime("%H:%M:%S")
            track.save()
        elif (track.is_working == True and track.is_ended == False):
            track.is_working = False
            track.is_ended = True
            track.end_time = strftime("%H:%M:%S")
            track.save()
        return Response('success')


class TimeTrackingList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, limit=10, page=1):

        if(self.request.query_params.get('limit')):
            limit = self.request.query_params.get('limit')
            items = StartDay.objects.filter(company=userCompany(self.request.user.pk))[:int(limit)]
        else:
            items = StartDay.objects.filter(company=userCompany(self.request.user.pk))

        return Response({
            'time_tracking_list': TimeTrackingListSerializer(items, many=True).data
        })



class TimeTrackingPropertiesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        property = TimeTrackingProperties.objects.get(company=userCompany(self.request.user.pk))
        return Response(
            TimeTrackingPropertySerializer(property, many=False).data
        )

    def put(self, request):
        try:
            instance = TimeTrackingProperties.objects.get(company=userCompany(self.request.user.pk))
        except:
            instance = ''

        property = TimeTrackingPropertySerializer(data=request.data, instance=instance)
        property.is_valid(raise_exception=True)
        property.save()
        return Response(
            'success'
        )


