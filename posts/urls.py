from django.urls import path
from .views import post_list, comment_list, post_detail, add_post, add_comment

urlpatterns = [
    path('', post_list, name="post-list"),
    path('<int:post_id>/', post_detail, name='post-detail'),
    path('<int:post_id>/comments/', comment_list, name='comment-list'),
    path('add-post/<int:user_id>/', add_post, name='add-post'),
    path('<int:post_id>/add-comment/', add_comment, name='add-comment'),
]
