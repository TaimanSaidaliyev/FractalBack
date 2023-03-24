from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/news/', include('news.urls')),
    # path('api/auth/', include('rest_framework.urls')),
    # path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/auth/', include('systemModules.urls')),
    path('api/profile/', include('userInformation.urls')),
    path('api/common/', include('common.urls')),
    path('api/project_management/', include('projectManagement.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
