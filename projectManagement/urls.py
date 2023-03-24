from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from projectManagement.views import *


urlpatterns = [
    path('tasks_list_by_project/<int:project_id>/', TaskListByProject.as_view()),
    path('project/<int:project_id>/task_add/', TaskAddByProject.as_view()),
    path('project_information/<int:project_id>/', ProjectInformationById.as_view()),
    path('project/<int:project_id>/task/<int:task_id>/', TaskDetailById.as_view()),
    path('project/<int:project_id>/task/<int:task_id>/timetracking/', TaskTimeTracking.as_view()),
    path('project/timetracking/<int:timetracking_id>/delete/', TaskTimeTracking.as_view()),
    path('project/skills/', include('projectManagement.userSkills.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)