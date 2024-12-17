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
    
    return JsonResponse({"code": 400})

def vote_scores(request, parent_type, id):
    if request.method == "POST":
        vote_type = request.POST.get('vote_type')
        
        if parent_type == "post":
            object = Post.objects.get(id=id)
            vote, created = Score.objects.get_or_create(post=object, user=request.user)
        elif parent_type == "comment":
            object = Comment.objects.get(id=id)
            vote, created = Score.objects.get_or_create(comment=object, user=request.user)
        
        if not created and vote.vote_type == vote_type:
            vote.delete()
        else:            
            vote.vote_type = vote_type
            vote.save()
        
        upvotes = object.votes.filter(vote_type='up').count()
        downvotes = object.votes.filter(vote_type='down').count()
        
        return JsonResponse({'upvotes': upvotes, 'downvotes': downvotes})
    
    return JsonResponse({"code": 400})
    
    
    
