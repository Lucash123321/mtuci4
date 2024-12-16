from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Q, Prefetch
from posts.models import Topic
from posts.views import get_full_post


def main(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, "index.html", context=context)

# FAST URL TEST PAGE
def test_urls(request):
    
    return render(request, "test_urls.html")
