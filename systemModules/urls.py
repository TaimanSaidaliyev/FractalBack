from django.urls import path, include
from .views import TokenList, CompanyInformationByUserId, UploadImage

urlpatterns = [
    path('verify_token/', TokenList.as_view()),
    path('company/', CompanyInformationByUserId.as_view()),
    path('propertybyuser/', include('systemModules.PropertiesByUser.urls')),
    path('upload_image/', UploadImage.as_view()),
]