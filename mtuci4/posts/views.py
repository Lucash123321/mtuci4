from django.shortcuts import render

# Create your views here.
def create_post(request):
    pass


def delete_post(request):  # for moderators only
    pass


def get_post(request, id):
    post = Post.objects.get(id=id)
    context = {"post": post}
    return render()


def get_posts(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render()

