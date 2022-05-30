from django.contrib import admin
from.views import PostDetailView, PostListView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from django.urls import path
from . views import home, about

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), 
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'), 
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('create/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', about, name='blog-about'),
]

