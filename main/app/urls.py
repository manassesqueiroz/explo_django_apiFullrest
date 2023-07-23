from django.urls import path
from . import views


urlpatterns = [
    path('user/', views.api_env, name='ver-criar=Users'),
    path('user/<str:id>/', views.api_mod, name='update-ver-delete=User'),
]
