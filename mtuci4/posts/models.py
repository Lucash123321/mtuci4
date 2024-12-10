from django.db import models
from django.conf import settings
from django.utils.timezone import now
from topics.models import Topic

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="post_author", on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, related_name="post_topic", on_delete=models.CASCADE)
    topic_post_id = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    date = models.DateTimeField(default=now)

    class Meta:
        unique_together = ('topic', 'topic_post_id')
    
    def is_comment(self):
        return self.parent is not None

    def save(self, *args, **kwargs):
        if not self.topic_post_id:
            max_id = Post.objects.filter(topic=self.topic).aggregate(models.Max('topic_post_id'))['topic_post_id__max']
            self.topic_post_id = (max_id or 0) + 1
        super().save(*args, **kwargs)

