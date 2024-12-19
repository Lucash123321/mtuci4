from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponseRedirect
from comments.models import Comment
from roles.models import Permission
from scores.models import Score
from topics.models import Topic
from posts.models import Post
from comments.forms import CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def create_comment(request):
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        text = request.POST.get('text')
        if len(text) == 0:
            return  JsonResponse({"code": 400})
        comment.text = text
        if request.POST.get("type") == 'post':
            comment.post = Post.objects.get(id=request.POST.get("id"))
        elif request.POST.get("type") == 'comment':
            comment.parent = Comment.objects.get(id=request.POST.get("id"))
        else:
            JsonResponse({"code": 400})
        
        comment.save()
        
        return JsonResponse({"code": 200})
    
    return JsonResponse({"code": 405})


@login_required
def edit_comment(request, comment_id):
    permission = Permission.objects.filter(role=request.user.role, entity='post', permission='edit')
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=comment_id)
        if not permission and request.user != comment.user:
            return JsonResponse({"code": 403})
        
        comment.text = request.POST.get("text")
        comment.save()
        return JsonResponse({"code": 200})
    return JsonResponse({"code": 405})


@login_required()
def delete_comment(request, comment_id):
    permission = Permission.objects.filter(role=request.user.role, entity='post', permission='delete')
    if request.method == "POST":
        comment = get_object_or_404(Comment, id=comment_id)
        Comment.objects.filter(parent=comment_id).delete()
        if not permission and request.user != comment.user:
            return JsonResponse({"code": 403})

        comment.delete()
        return JsonResponse({"code": 200})
    return JsonResponse({"code": 405})


@login_required
def vote_comment(request, comment_id, vote_type):

    if request.method != "POST":
        return JsonResponse({"code": 405})

    comment = get_object_or_404(Comment, id=id)
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
    