from . import views
from django.urls import path


urlpatterns = [
    path('', views.user_login, name='login'),
    path('base_file/', views.base_file, name='base_file'),
    path('register/', views.register, name='register'),
    path('user_logout', views.user_logout, name='user_logout'),
]

