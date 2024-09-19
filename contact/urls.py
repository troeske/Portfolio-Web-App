from . import views
from django.urls import path

urlpatterns = [
    path('', views.contact, name='contact'),
    path('collaboration_request_list/', views.collaboration_request_list, name='collaboration_request_list'),
]