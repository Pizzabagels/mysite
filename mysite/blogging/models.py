from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=120)
    text = models.CharField(blank=True, max_length=280)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, max_length=128)
    posts = models.ManyToManyField(Post, blank=True, related_name='categories')

    def __str__(self):
        return self.name
