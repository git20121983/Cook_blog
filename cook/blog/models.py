from itertools import count
from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey('self', related_name = "children", on_delete = models.SET_NULL, null = True, blank = True)
   
# // Отображает текстовое значение 
    def __str__(self):
        return self.name 
    
    class MPTTMeta:
        order_insertion_by = ['name']
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    
# // Отображает текстовое значение
    def __str__(self):
        return self.name 
#//
class Post(models.Model):
    author = models.ForeignKey(User, related_name = 'posts', on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'articles/')
    text = models.TextField()
    category = models.ForeignKey(Category, related_name = 'post', on_delete = models.SET_NULL, null = True)
    tags = models.ManyToManyField(Tag, related_name = 'post')
    create_at = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(max_length=200, default='')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_single", kwargs={"slug": self.category.slug, "post_slug":self.slug})
    

class Recipe(models.Model):
    name = models.CharField(max_length=150)
    serves = models.CharField(max_length=150)
    prep_time = models.PositiveIntegerField(default=0)
    cooc_time = models.PositiveBigIntegerField(default=0)
    ingredients = models.TextField()
    directions = models.TextField()
    post = models.ForeignKey(Post, related_name='recipe', on_delete=models.SET_NULL, null=True, blank=True)
    
    def trim8(self):
        return u"%s..."% (self.post.title[:8])
    
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=150)
    massege = models.TextField(max_length=500)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
   