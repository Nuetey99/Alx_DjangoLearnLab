"""
URL configuration for django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import PostDetailView, CommentUpdateView, CommentDeleteView , CommentCreateView

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='blog/login.html'), name = 'login'),
    path('logout', auth_views.LogoutView.as_view(template_name= 'blog/logout.html'), name = 'logout'),
    path('register/', views.register, name = 'register'),
    path ('profile/', views.profile, name = 'profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Missing URL for update
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/<int:comment_id>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('post/<int:pk>/comment/<int:comment_id>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:pk>/comment/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
]

