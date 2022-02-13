from django.urls import path 
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name="post-list"),
    path('new/', views.CreatePost.as_view(), name="new-post"),
    path('view/<slug:slug>', views.ViewPost.as_view(), name="view-post"),
    path('edit/<slug:slug>', views.UpdatePost.as_view(), name="edit-post"),
    path('delete/<slug:slug>', views.DeletePost.as_view(), name="delete-post"),
    path('tag/<str:tag>', views.tagged_posts, name='tag'),
]
