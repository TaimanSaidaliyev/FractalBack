from django.urls import path
from projectManagement.userSkills.views import *

urlpatterns = [
    path('access/', UserAccess.as_view()),
    path('questions/', TestQuestions.as_view()),
    path('questions_list/filter/<int:skill_id>/', TestAllQuestionsList.as_view()),
    path('questions_list/<int:id>/', TestQuestion.as_view()),
    path('questions/answer/<int:id>/', TestQuestionAnswer.as_view()),
    path('list/', SkillList.as_view()),
    path('item/<int:skill_id>/', SkillItem.as_view()),
    path('item/position/<int:position_id>/', SkillItemAdd.as_view()),
    path('item/project_position/list/', ProjectPositionList.as_view()),
    path('item/project_position/add/<int:project_id>/', ProjectPositionAdd.as_view()),
    path('item/project_position/<int:position_id>/', ProjectPositionItem.as_view()),
    path('item/project_position/<int:position_id>/<int:skill_id>/', ProjectPositionSkill.as_view()),
]