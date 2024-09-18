from . import views
from django.urls import path

urlpatterns = [
    path('', views.projects_list, name='projects_list'),
]