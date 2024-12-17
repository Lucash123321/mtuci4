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

def edit_post(request):  # for moderators only | upd by maksanik: "maybe for user who created too?"
    pass

def delete_post(request):  # for moderators only | upd by maksanik: "maybe for user who created too?"
    pass

def vote_post(request, topic_slug, id):
    topic = Topic.objects.get(slug=topic_slug)
    post = Post.objects.get(topic_post_id=id, topic=topic)

    if request.method == "POST":
        vote_type = request.POST.get('vote_type')
        vote, created = Score.objects.get_or_create(post=post, user=request.user)
        
        if not created and vote.vote_type == vote_type:
            vote.delete()
        else:            
            vote.vote_type = vote_type
            vote.save()
        
        upvotes = post.votes.filter(post=post, vote_type='up').count()
        downvotes = post.votes.filter(post=post, vote_type='down').count()
        return JsonResponse({'upvotes': upvotes, 'downvotes': downvotes})
    
    elif request.method == "GET":
        upvotes = post.votes.filter(post=post, vote_type='up').count()
        downvotes = post.votes.filter(post=post, vote_type='down').count()
        return JsonResponse({'upvotes': upvotes, 'downvotes': downvotes})
        
    return JsonResponse({"code": 400})

def get_user_vote(request, topic_slug, id):
    if request.method == "POST":
        current_user = request.user
        topic = Topic.objects.get(slug=topic_slug)
        post = Post.objects.get(topic=topic, topic_post_id=id)
        try:
            current_score = Score.objects.get(user=current_user, post=post)
        except Score.DoesNotExist:
            current_score = None
        
        print(current_score)
        return JsonResponse({})

def post_detail(request, topic_slug, id):
    topic = Topic.objects.get(slug=topic_slug)
    post = Post.objects.get(topic=topic, topic_post_id=id,)
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