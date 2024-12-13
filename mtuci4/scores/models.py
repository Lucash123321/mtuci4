from django.db import models

from posts.models import Post
from users.models import CustomUser

# Create your models here.

class Score(models.Model):
    CHOICES = (
        ('up', 'Upvote'),
        ('down', 'Downvote'),
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=10, choices=CHOICES)

    class Meta:
        unique_together = ('post', 'user')