from . import views
from django.urls import path

urlpatterns = [
    path('', views.consultant_home, name='home'),
    path('about/', views.consultant_about, name='about'),
    path('reload-config/', views.reload_config, name='reload_config'),
]