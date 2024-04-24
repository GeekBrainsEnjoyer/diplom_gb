from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': "w-full h-12  p-3 border border-gray-300 rounded-xl",
            'placeholder': 'Комментарий...',
        }))

    class Meta:
        model = Comment
        fields = ['content']
