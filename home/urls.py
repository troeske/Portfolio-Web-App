from . import views
from django.urls import path

urlpatterns = [
    path('', views.consultant_home, name='home'),
    path('reload-config/', views.reload_config, name='reload_config'),
]