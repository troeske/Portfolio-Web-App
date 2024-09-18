from . import views
from django.urls import path

urlpatterns = [
    path('', views.projects_list, name='projects_list'),
    path('<slug:slug>/', views.project_details, name="project_details"),
]