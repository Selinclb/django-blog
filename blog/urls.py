from django.urls import path
from . import views
from .views import TaggedPostsView

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('posts/', views.post_list, name='post_list'), 
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'), 
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('tag/<int:tag_id>/', TaggedPostsView.as_view(), name='tagged_posts'),
    
    
]
