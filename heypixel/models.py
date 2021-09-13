from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

# Create your models here.

class User(AbstractUser):
	image = CloudinaryField('imagen', default=True, blank=True)
	bio = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return str(self.user.username)


class Post (models.Model):
    body = models.TextField(max_length=1000, blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='author', blank=True)
    image = CloudinaryField('imagen', default=True, blank=True)

    def __str__ (self):
        return self.author.username

class Comment(models.Model):
    body_comment = models.TextField(max_length=1000, blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_on']

class Like(models.Model):
    like_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes", blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes", blank=True, null=True)


