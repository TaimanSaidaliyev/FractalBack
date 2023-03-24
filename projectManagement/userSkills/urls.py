from django.urls import path
from projectManagement.userSkills.views import *

urlpatterns = [
    path('access/', UserAccess.as_view()),
    path('questions/', TestQuestions.as_view()),
]