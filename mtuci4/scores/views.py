from django.shortcuts import render
from django.http import JsonResponse
from posts.models import Post
from scores.models import Score
from comments.models import Comment


def get_scores(request, parent_type, id):
    if request.method == "GET":
        if parent_type == "post":
            object = Post.objects.get(id=id)
        elif parent_type == "comment":
            object = Comment.objects.get(id=id)
            
        upvotes = object.votes.filter(vote_type='up').count()
        downvotes = object.votes.filter(vote_type='down').count()
        print(upvotes, downvotes)
        return JsonResponse({'upvotes': upvotes, 'downvotes': downvotes})
    return JsonResponse({"parent_type": parent_type, "id": id})

def vote_scores(request, parent_type, id):
    if request.method == "POST":
        vote_type = request.POST.get('vote_type')
        
        if parent_type == "post":
            post = Post.objects.get(id=id)
            vote, created = Score.objects.get_or_create(post=post, user=request.user)
        elif parent_type == "comment":
            pass
        
        if not created and vote.vote_type == vote_type:
            vote.delete()
        else:            
            vote.vote_type = vote_type
            vote.save()
        
        upvotes = post.votes.filter(post=post, vote_type='up').count()
        downvotes = post.votes.filter(post=post, vote_type='down').count()
        return JsonResponse({'upvotes': upvotes, 'downvotes': downvotes})
    
    
    
