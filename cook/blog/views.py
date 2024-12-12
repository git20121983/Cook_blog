from datetime import *
from django.utils import timezone
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post




# Create your views here.

class PostListView(ListView):
    model = Post
    queryset = Post.objects.annotate(comments_count=Count('comment_set')).all()
    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related("category")
    
    
        
class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    slug_url_kwarg = 'post_slug'
    
    

def home (request):
    return render(request, 'base.html')