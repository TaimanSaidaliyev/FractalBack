from django.contrib import admin
from .models import Comment, CommonFiles, FileIcon

admin.site.register(Comment)
admin.site.register(CommonFiles)
admin.site.register(FileIcon)