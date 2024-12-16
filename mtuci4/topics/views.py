from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Q, Prefetch
from topics.models import Topic
from posts.views import get_full_post


# Create your views here.
# def main(request):
#     topics = Topic.objects.all()
#     context = {'topics': topics}
#     return render(request, "index.html", context=context)

def topic(request, slug):
    topic = Topic.objects.get(slug=slug)

    posts = topic.post_topic.filter(topic=topic, parent=None).annotate(
        upvotes=Count('votes', filter=Q(votes__vote_type='up')),
        downvotes=Count('votes', filter=Q(votes__vote_type='down'))
    )

    posts_with_comments = get_full_post(request, posts)

    return render(request, 'topics/topic.html', {'posts': posts_with_comments, 'topic': topic})
    

def post(request):
    return render(request, "posts/post.html")


def add_comment(request):
    pass


def upvote(request):
    pass


def downvote(request):
    pass
