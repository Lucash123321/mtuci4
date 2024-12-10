from django import forms

from posts.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['topic', 'title', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description']
