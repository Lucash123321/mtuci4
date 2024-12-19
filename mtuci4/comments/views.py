from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from comments.models import Comment
from scores.models import Score
from django.contrib.auth.decorators import login_required

# Create your views here.

def create_comment(request):
    pass

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


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != Comment.user:
        return JsonResponse({"code": 403})

    comment.text = request.POST.text
    comment.save()

@login_required()
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != Comment.user:
        return JsonResponse({"code": 403})

    comment.delete()

@login_required
def vote_comment(request, id, vote_type):

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
    