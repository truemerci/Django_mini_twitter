from django.shortcuts import render, get_object_or_404, redirect

from posts.forms import PostForm, CommentForm
from posts.models import Post, Comment


def home(request):
    return render(request, 'home.html')


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments})


def comment_list(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'posts/comment_list.html', {'post': post, 'comments': comments})


def add_post(request, user_id):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.user_id = user_id
            form.save()
            return redirect('user-detail', user_id=user_id)
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


def add_comment(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.post = post
            comment = form.save()
            post = comment.post
            return redirect('post-detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'posts/create_comment.html', {'form': form, 'post': post})

