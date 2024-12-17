from django.db import models

from posts.models import Post
from comments.models import Comment
from users.models import CustomUser

# Create your models here.

class Score(models.Model):
    CHOICES = (
        ('up', 'Upvote'),
        ('down', 'Downvote'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes', null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='votes', null=True, blank=True)
    vote_type = models.CharField(max_length=10, choices=CHOICES)

    class Meta:
        unique_together = ('post', 'user', 'comment')  
        
    def save(self, *args, **kwargs):
        # Убедиться, что только одно из полей post или comment заполнено
        if self.post and self.comment:
            raise ValueError("You cannot assign both a post and a comment to a rating.")
        if not self.post and not self.comment:
            raise ValueError("You must assign either a post or a comment to a rating.")
        super().save(*args, **kwargs)