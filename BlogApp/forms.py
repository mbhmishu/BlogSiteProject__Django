from django import forms
from BlogApp.models import Comment, Likes

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


