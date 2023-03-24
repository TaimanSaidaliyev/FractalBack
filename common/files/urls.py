from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import CommonFilesView

urlpatterns = [
    path('view/<int:record_id>/<int:module_id>/', CommonFilesView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
