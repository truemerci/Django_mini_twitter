from django.shortcuts import render, get_object_or_404
from users.models import User
from posts.models import Post


def home(request):
    return render(request, 'users/home.html')


def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    posts = Post.objects.filter(user=user)
    return render(request, 'users/user_detail.html', {'user': user, 'posts': posts})


def user_posts(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    posts = Post.objects.filter(user=user)
    return render(request, 'users/user_posts.html', {'user': user, 'posts': posts})


