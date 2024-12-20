from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm
from posts.models import Post
from roles.models import Permission
from django.http import JsonResponse
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404
from topics.models import Topic

def check_permission(request, permission):
    permission = Permission.objects.filter(role=request.user.role, entity='post', permission=permission)
    return True if permission else False

# TODO: Адаптировать к текущим реалиям
@login_required
def create_post(request, topic_slug):
    topic = get_object_or_404(Topic, slug=topic_slug)
    
    posts = topic.posts.filter(topic=topic).annotate(
        upvotes=Count('votes', filter=Q(votes__vote_type='up')),
        downvotes=Count('votes', filter=Q(votes__vote_type='down'))
    )

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.topic = topic
            post.save()
            return redirect('topics:topic', slug=topic.slug)
    else:
        form = PostForm()
    
    context = {
        'topic': topic, 
        'posts': sorted(posts, reverse=True, key=lambda x: x.id),
        'form': form,
    }

    return render(request, 'topics/topic.html', context=context)


@login_required
def edit_post(request, topic_slug, post_id):  # for moderators only | upd by maksanik: "maybe for user who created too?"
    permission = Permission.objects.filter(role=request.user.role, entity='post', permission='edit')
    if request.method == "POST":
        topic = Topic.objects.get(slug=topic_slug)
        post = Post.objects.get(topic=topic, topic_post_id=post_id)

        if not permission and post.user != request.user:
            return JsonResponse({'code': 403})
        
        post.title = request.POST.get("title")
        post.text = request.POST.get("text")
        post.save()
        return JsonResponse({'code': 200})
    return JsonResponse({'code': 405})


@login_required
def delete_post(request, topic_slug, post_id):  # for moderators only | upd by maksanik: "maybe for user who created too?"
    permission = Permission.objects.filter(role=request.user.role, entity='post', permission='delete')
    if request.method == "POST":
        topic = Topic.objects.get(slug=topic_slug)
        post = Post.objects.get(topic=topic, topic_post_id=post_id)

        if not permission and post.user != request.user:
            return JsonResponse({'code': 403, 'redirect_url': topic_slug})

        post.delete()
        return JsonResponse({'code': 200, 'redirect_url': topic_slug})
    return JsonResponse({'code': 405})


def post_detail(request, topic_slug, id):
    if not request.user.is_authenticated:
        redirect('users:login')
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