from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('users/', views.user_list, name="user-list"),
    path('users/<int:user_id>/', views.user_detail, name='user-detail'),
    path('users/<int:user_id>/posts/', views.user_posts, name='user-posts'),
]
