from django import forms

from .models import ChatMessage


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ('message', )
        widgets = {
            'message': forms.Textarea(attrs={
                'class': "w-full h-12  p-3 border border-gray-300 rounded-xl",
                'placeholder': 'Введите сообщение...',})
        }
