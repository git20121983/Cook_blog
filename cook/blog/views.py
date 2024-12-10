from django.shortcuts import render
from django.views.generic import ListView

from cook.blog.models import Post


# Create your views here.

class PostListView(ListView):
    model = Post

def home (request):
    return render(request, 'base.html')