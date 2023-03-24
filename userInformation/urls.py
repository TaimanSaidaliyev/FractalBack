from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from userInformation.views import ProfileInformation, ProfileCurrentUser, ProfileInformationForWidgets
from userInformation.timeTracking.views import TimeTrackingUser, TimeTrackingList, TimeTrackingPropertiesView


urlpatterns = [
    path('<int:pk>/', ProfileInformation.as_view()),
    path('short/<int:pk>/', ProfileInformationForWidgets.as_view()),
    path('', ProfileCurrentUser.as_view()),
    path('timetracking/', TimeTrackingUser.as_view()),
    path('timetracking/list/', TimeTrackingList.as_view()),
    path('timetracking/property/', TimeTrackingPropertiesView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)