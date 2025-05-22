from django import forms

from .models import Comment, Topic

class CreateTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            'title', 'description'
        ]


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body', 'author', 'post'
        ]