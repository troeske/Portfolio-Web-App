from .models import CollaborationRequest
from django import forms

class CollaborationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = CollaborationRequest
        fields = ('first_name', 'last_name', 'email', 'message')