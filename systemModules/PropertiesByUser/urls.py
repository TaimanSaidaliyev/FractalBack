from django.urls import path
from .views import PropertyItemPut, PropertyItemGet

urlpatterns = [
    path('put/<int:type_id>/<int:module_id>/<int:record_id>/', PropertyItemPut.as_view()),
    path('get/<int:type_id>/<int:module_id>/<int:record_id>/', PropertyItemGet.as_view()),
]