from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class PostListView(ListView):
    model = models.Post
    context_object_name = "posts"
    template_name = "blog/blog_list.html"

class PostDetailView(DetailView):
    model = models.Post
    template_name = "blog/blog_detail.html"

    """
    By default DetailView will provide a context object
    we can use in our template called either object or the lowercased name of our model,
    which would be 'post'. Also, DetailView expects either a primary key or a slug passed
    to it as the identifier.

    If you find using post or object confusing, it’s possible to explicitly name the context
    object in our view using context_object_name.
    """

class PostCreateView(CreateView):
    #https://docs.djangoproject.com/en/2.2/ref/class-based-views/generic-editing/
    model = models.Post
    template_name = "blog/post_create.html"
    fields = ["title", "author", "text"] #these are three of the variables from the Post class in models.py.

class PostEditView(UpdateView):
    model = models.Post
    template_name = "blog/post_edit.html"
    fields = ["title", "text"]

class DeletePostView(DeleteView):
    model = models.Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("home")
    """
    We use reverse_lazy as opposed to just reverse so that it won’t execute the URL
    redirect until our view has finished deleting the blog post.
    """
