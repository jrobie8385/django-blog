from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView
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
