from django.shortcuts import render
from django.http import JsonResponse
from comments.models import Comment
from scores.models import Score

# Create your views here.

def create_comment(request):
    pass

def vote_comment(request, id, vote_type):
    if request.method == "POST":
        comment = Comment.objects.get(id=id)
        vote, created = Score.objects.get_or_create(comment=comment, user=request.user)
        removed = False
        if not created and vote.vote_type == vote_type:
            vote.delete()
            removed = True
        else:            
            vote.vote_type = vote_type
            vote.save()
            
        upvotes = comment.votes.filter(comment=comment, vote_type='up').count()
        downvotes = comment.votes.filter(comment=comment, vote_type='down').count()
        return JsonResponse({'upvotes': upvotes, 'downvotes': downvotes, 'removed': removed})
    return JsonResponse({"code": 400})