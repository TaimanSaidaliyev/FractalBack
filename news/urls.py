from django.urls import path
from news.views import NewsList, NewSingle, NewComments, NewAdd, NewDelete, NewUpdate, NewsAllList, CategoryList, \
    NewsListByCategory, SetViewNew
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', NewsList.as_view()),
    path('all/', NewsAllList.as_view()),
    path('add/', NewAdd.as_view()),
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', NewsListByCategory.as_view()),
    path('<int:pk>/', NewSingle.as_view()),
    path('<int:pk>/setview/', SetViewNew.as_view()),
    path('<int:pk>/update/', NewUpdate.as_view()),
    path('<int:pk>/delete/', NewDelete.as_view()),
    path('<int:pk>/comments/', NewComments.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
