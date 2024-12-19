from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Q
from topics.models import Topic


# Create your views here.

def topic(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    
    posts = topic.posts.filter(topic=topic).annotate(
        upvotes=Count('votes', filter=Q(votes__vote_type='up')),
        downvotes=Count('votes', filter=Q(votes__vote_type='down'))
    )
    
    context = {
        'topic': topic, 
        'posts': sorted(posts, reverse=True, key=lambda x: x.id)
    }

    return render(request, 'topics/topic.html', context=context)


