from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count, Q
from posts.forms import CommentForm, PostForm
from posts.models import Post
from scores.models import Score
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

def delete_post(request):  # for moderators only
    pass

def vote_post(request, topic_slug, id, vote_type):
    if request.method == "POST":
        topic = Topic.objects.get(slug=topic_slug)
        post = Post.objects.get(topic_post_id=id, topic=topic)
        vote, created = Score.objects.get_or_create(post=post, user=request.user)
        removed = False
        if not created and vote.vote_type == vote_type:
            vote.delete()
            removed = True
        else:            
            vote.vote_type = vote_type
            vote.save()
        upvotes = post.votes.filter(post=post, vote_type='up').count()
        downvotes = post.votes.filter(post=post, vote_type='down').count()
        return JsonResponse({'upvotes': upvotes, 'downvotes': downvotes, 'removed': removed})
    return JsonResponse({"code": 400})

# TODO: Протестить с формами, Адаптировать к текущим реалиям
# @login_required
# def create_comment(request, topic_slug, id):
#     topic = Topic.objects.get(slug=topic_slug)
#     parent = Post.objects.get(topic_post_id=id, topic=topic)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.parent = parent
#             comment.topic = parent.topic
#             comment.save()
#             return redirect('post_detail', topic_id=parent.id)
#     else:
#         form = CommentForm()
#     return render(request, 'posts/create_comment.html', {'form': form})

def post_detail(request, topic_slug, id):
    topic = Topic.objects.get(slug=topic_slug)
    post = Post.objects.get(topic=topic, topic_post_id=id, )
    user_vote = post.votes.filter(user=request.user).first()
    post.user_vote_type = user_vote.vote_type if user_vote else None
    upvotes = post.votes.filter(vote_type='up').count()
    downvotes = post.votes.filter(vote_type='down').count()
    return render(request, 'posts/post_detail.html', {
        'topic': topic,
        'post': post,
        'upvotes': upvotes,
        'downvotes': downvotes
    })