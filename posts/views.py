from dataclasses import field
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from .models import Post 

class CreatePost(CreateView):
    fields = "__all__"
    model = Post 

class PostList(ListView):
    model = Post 

class ViewPost(DetailView):
    model = Post 

class UpdatePost(UpdateView):
    fields = "__all__"
    model = Post 

class DeletePost(DeleteView):
    model = Post 
    success_url = reverse_lazy('posts:post-list')

def tagged_posts(request, tag):
    post_list = Post.objects.filter(tags__name__in=[tag])
    return render(request, 'posts/tagged_posts.html', context={'post_list': post_list, 'tag': tag})
    