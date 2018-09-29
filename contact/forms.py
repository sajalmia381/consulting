from django import forms
from .models import FormContact, Quote
from service.models import Service
from django.utils.translation import gettext as _


class ContactForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name: '}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email :'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message :'}))

    class Meta:
        model = FormContact
        fields = ['name', 'email', 'message']
        # widgets = {
        #     'name': forms.TextInput(attrs={'placeholder': 'Full Name :'}),
        #     'email': forms.EmailInput(attrs={'placeholder': 'Your Email :'}),
        #     'message': forms.Textarea(attrs={'placeholder': 'Message :'})
        # }
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }

    # --------------- Validation

    def clean_name(self):
        name = self.cleaned_data.get('name')
        # if name is not None:
        #     return name
        # else:
        #     raise forms.ValidationError('Must Have a name')

        if len(name) <= 5:
            raise forms.ValidationError('Name is Too Short')
        return name

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not email:
    #         raise forms.ValidationError('Email Field is not be empty')
    #     elif not '@' and '.' in email:
    #         raise forms.ValidationError('Must Have a valid Email address')
    #     else:
    #         return email


class QuoteForm(forms.ModelForm):
    # service = forms.ModelChoiceField(queryset=Service.objects.all())

    class Meta:
        model = Quote
        fields = [
            'service', 'name', 'email', 'number'
        ]

        widgets = {
            'service': forms.SelectMultiple(attrs={'placeholder': 'Services'}),
            'name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'number': forms.NumberInput(attrs={'placeholder': 'Your Number'}),
            # 'description': forms.Textarea(attrs={'placeholder': 'Something About project', 'cols': '100%'})
        }


class QuoteFormNew(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['service', 'name', 'email', 'number']