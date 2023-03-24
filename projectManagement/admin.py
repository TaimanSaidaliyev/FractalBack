from django.contrib import admin
from projectManagement.models import *

admin.site.register(Project)
admin.site.register(Tasks)
admin.site.register(TimeTracking)
admin.site.register(Status)
admin.site.register(Priority)
admin.site.register(Category)
admin.site.register(UserSelfCategory)
admin.site.register(UserSelfCategoryDictionary)
admin.site.register(UserSelfSavedTasks)
admin.site.register(TaskChangeHistory)
admin.site.register(TaskChangeHistoryAction)
admin.site.register(TaskApproveStatus)
admin.site.register(TaskApproveStatusActions)
admin.site.register(TaskAnswerByExecutors)

admin.site.register(ProjectPosition)
admin.site.register(Skills)
admin.site.register(SkillQuestion)
admin.site.register(SkillQuestionAnswers)
admin.site.register(ProjectPositionUsers)
admin.site.register(SkillUserAnswers)
