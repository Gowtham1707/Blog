from django import forms

from .models import comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['user_name', 'email', 'text']
        labels = {
            "user_name": 'Your Name',
            "email": 'Your Email',
            "text": 'Your Comment',
        }