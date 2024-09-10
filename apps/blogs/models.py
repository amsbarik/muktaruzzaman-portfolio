from django.contrib.auth.models import User  # Assuming you're using Django's built-in User model
from django.db import models

from django.utils import timezone
from datetime import timedelta

class Blog(models.Model):
    title = models.CharField(max_length=120)
    thumbnail = models.ImageField(upload_to='blogs', default='defaults/blog-thumbnail.jpg')
    short_desc = models.TextField()
    
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    shares = models.PositiveIntegerField(default=0, blank=True, null=True)
    
    order = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    tags = models.ManyToManyField('Tag', related_name='blogs', blank=True)
    category = models.ForeignKey('Category', related_name='blogs', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.title

    def time_since_published(self):
        now = timezone.now()
        diff = now - self.created_at

        if diff < timedelta(minutes=1):
            return f'{int(diff.seconds)} seconds ago'
        elif diff < timedelta(hours=1):
            return f'{int(diff.seconds / 60)} minutes ago'
        elif diff < timedelta(days=1):
            return f'{int(diff.seconds / 3600)} hours ago'
        elif diff < timedelta(days=2):
            return 'Yesterday'
        elif diff < timedelta(weeks=1):
            return f'{diff.days} days ago'
        elif diff < timedelta(weeks=2):
            return '1 week ago'
        elif diff < timedelta(weeks=4):
            return f'{int(diff.days / 7)} weeks ago'
        elif diff < timedelta(days=60):
            return '1 month ago'
        else:
            return f'{int(diff.days / 30)} months ago'



class BlogContent(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, related_name='blog_content')
    heading = models.CharField(max_length=255)
    cover_photo = models.ImageField(upload_to='blogs', default='defaults/blog-cover-photo.jpg', blank=True, null=True)
    content = models.TextField(blank=True, null=True) 
    content2 = models.TextField(blank=True, null=True, default='') 
    
    code_heading = models.CharField(max_length=120, null=True, blank=True)
    code_txt = models.TextField(blank=True, null=True)  
    code_img = models.ImageField(upload_to='blogs', blank=True, null=True)
    
    key_heading = models.CharField(max_length=120, null=True, blank=True)
    key_txt = models.TextField(blank=True, null=True)
    key_img = models.ImageField(upload_to='blogs', null=True, blank=True)
    key_point1 = models.CharField(max_length=255, blank=True, null=True)
    key_point2 = models.CharField(max_length=255, blank=True, null=True)
    key_point3 = models.CharField(max_length=255, blank=True, null=True)
    key_point4 = models.CharField(max_length=255, blank=True, null=True)
    key_point5 = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f'Comment by {self.user.username} on {self.blog.title}'



class Tag(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name



class Subscribe(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    email = models.EmailField()
    
    def __str__(self):
        return self.email