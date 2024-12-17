from django.shortcuts import render
from posts.models import Topic


def main(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, "index.html", context=context)

# FAST URL TEST PAGE
def test_urls(request):
    
    return render(request, "test_urls.html")
