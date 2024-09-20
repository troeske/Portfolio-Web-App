from . import views
from django.urls import path

urlpatterns = [
    path('', views.projects_list, name='projects_list'),
    path('<slug:slug>/', views.project_details, name="project_details"),
    path('client_registration_list', views.client_registration_list, name='client_registration_list'),
    path('delete_client/<str:username>',
         views.client_delete, name='client_delete'),
    path('approve_client/<client:client>',
        views.approve_client, name='approve_client'),
]