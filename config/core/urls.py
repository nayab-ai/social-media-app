from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/like/<int:post_id>/', views.like_post, name='like_post'),
    path('post/comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('follow/<str:username>/', views.follow_user, name='follow_user'),
    path('unfollow/<str:username>/', views.unfollow_user, name='unfollow_user'),
]