from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Profile, Post, Comment, Follow

# Home Page - YEH FUNCTION HONA CHAHIYE
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'core/home.html', {'posts': posts})

# Signup
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            return render(request, 'core/signup.html', {'error': 'Username already exists'})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user)
        login(request, user)
        return redirect('home')
    
    return render(request, 'core/signup.html')

# Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'core/login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'core/login.html')

# Logout
def user_logout(request):
    logout(request)
    return redirect('login')

# Create Post
@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST['content']
        Post.objects.create(user=request.user, content=content)
    return redirect('home')

# Like Post
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({'liked': liked, 'total_likes': post.total_likes()})

# Add Comment
@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        content = request.POST['content']
        Comment.objects.create(post=post, user=request.user, content=content)
    return redirect('home')

# Profile Page
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=profile_user).order_by('-created_at')
    
    is_following = False
    if request.user.is_authenticated:
        is_following = Follow.objects.filter(follower=request.user, following=profile_user).exists()
    
    followers_count = Follow.objects.filter(following=profile_user).count()
    following_count = Follow.objects.filter(follower=profile_user).count()
    
    context = {
        'profile_user': profile_user,
        'posts': posts,
        'is_following': is_following,
        'followers_count': followers_count,
        'following_count': following_count,
    }
    return render(request, 'core/profile.html', context)

# Follow User
@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    if user_to_follow != request.user:
        Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
    return redirect('profile', username=username)

# Unfollow User
@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)
    Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
    return redirect('profile', username=username)