from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Like, Category,Follow


# Create your views here.

# Home Page (Blog List)
@login_required
def home(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'blog_list.html', {'posts': posts})


# Register
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')

    return render(request, 'register.html')


# Login
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


# Logout
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def add_post(request):

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('cover_image')

        Post.objects.create(
            author=request.user,
            title=title,
            content=content,
            cover_image=image
        )

        return redirect('home')

    return render(request, 'add_blog.html')


# Blog Detail
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post)

    return render(request, 'blog_detail.html', {
        'post': post,
        'comments': comments
    })


# Edit Post
@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    categories = Category.objects.all()

    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.category_id = request.POST.get('category')

        if request.FILES.get('cover_image'):
            post.cover_image = request.FILES.get('cover_image')

        post.save()
        return redirect('home')

    return render(request, 'edit_blog.html', {'post': post, 'categories': categories})


# Delete Post
@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    post.delete()
    return redirect('home')


# Like Post
@login_required
def like_post(request, id):
    post = get_object_or_404(Post, id=id)

    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        like.delete()

    return redirect('post_detail', id=id)


# Add Comment
@login_required
def add_comment(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        text = request.POST.get('comment')

        Comment.objects.create(
            post=post,
            user=request.user,
            comment=text
        )

    return redirect('post_detail', id=id)

@login_required
def follow_user(request, id):
    user_to_follow = get_object_or_404(User, id=id)

    follow, created = Follow.objects.get_or_create(
        follower=request.user,
        following=user_to_follow
    )

    if not created:
        follow.delete()

    return redirect('home')