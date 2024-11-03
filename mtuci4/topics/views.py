from django.shortcuts import render, get_object_or_404
from topics.models import Topic

# Create your views here.
def main(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, "index.html", context=context)


def topic(request, slug):
    get_object_or_404(Topic, slug=slug)
    topic = Topic.objects.get(slug=slug)
    context = {"topic": topic}
    return render(request, "topics/topic.html", context)
    

def post(request):
    return render(request, "posts/post.html")


def add_comment(request):
    pass


def upvote(request):
    pass


def downvote(request):
    pass
