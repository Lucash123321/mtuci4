from django.db import models
from django.conf import settings
from django.utils.timezone import now
from topics.models import Topic

# Create your models here.
class Post(models.Model):
    topic = models.ForeignKey(Topic, related_name="posts", on_delete=models.CASCADE)
    topic_post_id = models.PositiveIntegerField(editable=False, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default=now)
    
    def __str__(self):
        return f"Post by {self.user} on {self.topic} by "

    class Meta:
        unique_together = ('topic', 'topic_post_id')
        ordering = ('-id',)

    def save(self, *args, **kwargs):
        if not self.topic_post_id:
            max_id = Post.objects.filter(topic=self.topic).aggregate(models.Max('topic_post_id'))['topic_post_id__max']
            self.topic_post_id = (max_id or 0) + 1
        super().save(*args, **kwargs)

