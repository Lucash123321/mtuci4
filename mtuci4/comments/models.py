from django.db import models
from django.conf import settings

# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comment_author", on_delete=models.CASCADE)
    text = models.TextField()
