from django.contrib import admin
from .models import Department, Honor, Status, Gender, JobTitle, Certificate, Profile

admin.site.register(Department)
admin.site.register(Honor)
admin.site.register(Status)
admin.site.register(Gender)
admin.site.register(JobTitle)
admin.site.register(Certificate)
admin.site.register(Profile)