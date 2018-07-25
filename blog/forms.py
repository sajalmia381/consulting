from django import forms
from .models import Comment, Reply


class ParentCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['full_name', 'email', 'text',]

        widgets = {
            'full_name': forms.TextInput(attrs={"placeholder": 'Full Name :'}),
            'email': forms.EmailInput(attrs={"placeholder": 'Your Email :'}),
            'text': forms.Textarea(attrs={'placeholder': 'Comment Here :'})
        }


class ChildCommentForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['full_name', 'email', 'text',]

        widgets = {
            'full_name': forms.TextInput(attrs={"placeholder": 'Full Name :'}),
            'email': forms.EmailInput(attrs={"placeholder": 'Your Email :'}),
            'text': forms.Textarea(attrs={'placeholder': 'Comment Here :'})
        }