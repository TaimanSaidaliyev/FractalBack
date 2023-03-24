from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import CommentsView

urlpatterns = [
    path('view/<int:record_id>/<int:module_id>/', CommentsView.as_view()),
    path('view/<int:record_id>/<int:module_id>/<int:pk>/', CommentsView.as_view()),
    path('delete/<int:pk>/', CommentsView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
