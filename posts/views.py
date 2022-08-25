from django.shortcuts import render
from django.views.generic import ListView

from posts.models import Post

# Create your views here.
class HomePageView(ListView):
    model= Post
    template_name= 'index.html'
    context_object_name = 'posts'
