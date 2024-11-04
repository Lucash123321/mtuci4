from django.db import models
from django.conf import settings
from topics.models import Topic

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="post_author", on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, related_name="post_topic", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
