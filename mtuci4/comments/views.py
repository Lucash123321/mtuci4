from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponseRedirect
from comments.models import Comment
from scores.models import Score
from topics.models import Topic
from posts.models import Post
from comments.forms import CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            if request.POST.type == 'post':
                comment.post = request.POST.id
            elif request.POST.type == 'parent':
                comment.parent = request.POST.parent
            else:
                JsonResponse({"code": 400})
            comment.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = CommentForm()
    return render(request, 'posts/create_comment.html', {'form': form})


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != Comment.user:
        return JsonResponse({"code": 403})

    comment.text = request.POST.text
    comment.save()
    return JsonResponse({"code": 200})

@login_required()
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != Comment.user:
        return JsonResponse({"code": 403})

    comment.delete()
    return JsonResponse({"code": 200})

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
    