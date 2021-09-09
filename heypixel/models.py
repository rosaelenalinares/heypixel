from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Post (models.Model):
    body = models.TextField(max_length=1000, blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='author')
    image = CloudinaryField('imagen', default=True)

    def __str__ (self):
        return self.author.username

class Comment(models.Model):
    body_comment = models.TextField(max_length=1000, blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_on']

class Like(models.Model):
    like_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10, blank=True, null=True)
    last_name = models.CharField(max_length=10, blank=True, null=True)
    bio = models.TextField(max_length=150, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=50, blank=True, null=True)


