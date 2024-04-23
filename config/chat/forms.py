from django import forms

from .models import ChatMessage


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ('message', )

    message = forms.Textarea(attrs={'class': 'w-full py-2 px-7 rounded-xl'})