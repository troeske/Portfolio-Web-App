from . import views
from django.urls import path

urlpatterns = [
    path('', views.contact, name='contact'),
    path('collaborationrequest_list/', views.collaborationcequest_list, name='collaborationrequest_list'),
]