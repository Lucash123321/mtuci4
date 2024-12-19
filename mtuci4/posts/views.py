from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm
from posts.models import Post
from roles.models import Permission
from django.http import JsonResponse
from topics.models import Topic


# TODO: Адаптировать к текущим реалиям
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list', topic_id=post.topic.id)
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def edit_post(request, topic_slug, post_id):  # for moderators only | upd by maksanik: "maybe for user who created too?"
    permission = Permission.objects.get(role=request.user.role, entity='post', permission='edit')
    if request.method == "POST":
        topic = Topic.objects.get(slug=topic_slug)
        post = Post.objects.get(topic=topic, topic_post_id=post_id)

        if not permission and post.user != request.user:
            return JsonResponse({'code': 403})

        post.title = request.POST.title
        post.text = request.POST.text
        post.save()
        return JsonResponse({'code': 200})
    return JsonResponse({'code': 405})


@login_required
def delete_post(request, topic_slug, post_id):  # for moderators only | upd by maksanik: "maybe for user who created too?"
    permission = Permission.objects.get(role=request.user.role, entity='post', permission='delete')
    if request.method == "POST":
        topic = Topic.objects.get(slug=topic_slug)
        post = Post.objects.get(topic=topic, topic_post_id=post_id)

        if not permission and post.user != request.user:
            return JsonResponse({'code': 403})

        post.delete()
        return JsonResponse({'code': 200})
    return JsonResponse({'code': 405})


def post_detail(request, topic_slug, id):
    topic = Topic.objects.get(slug=topic_slug)
    post = Post.objects.get(topic=topic, topic_post_id=id,)
    user_vote = post.votes.filter(user=request.user).first()
    post.user_vote_type = user_vote.vote_type if user_vote else None
    upvotes = post.votes.filter(vote_type='up').count()
    downvotes = post.votes.filter(vote_type='down').count()
    return render(request, 'posts/post_detail.html', {
        # 'topic': topic,
        'post': post,
        'upvotes': upvotes,
        'downvotes': downvotes
    })