from allauth.account.forms import SignupForm
from django import forms
from collections import OrderedDict
from django.core.mail import send_mail

class CustomSignupForm(SignupForm):
    """
    customizing the signup form to show first name and last name 
    suggested by github copilot.
    removing the ('optional') from email field to encourage the user 
    to fill it out for later use
    
    """
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    email = forms.EmailField(required=True, label='Your Email')

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Your Email'
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['first_name'].label = 'First Name'
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First Name'})
        self.fields['last_name'].label = 'Last Name'
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last Name'})
        self.fields['password1'].label = 'Password'
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].label = 'Password Confirmation'
        self.fields['password2'].widget.attrs.update({'placeholder': 'Password Confirmation'})

        self.fields = OrderedDict([
            ('username', self.fields['username']),
            ('first_name', self.fields['first_name']),
            ('last_name', self.fields['last_name']),
            ('email', self.fields['email']),
            ('password1', self.fields['password1']),
            ('password2', self.fields['password2']),
        ])

            
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user