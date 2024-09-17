from . import views
from django.urls import path

urlpatterns = [
    path('', views.consultant_home, name='home'),
]