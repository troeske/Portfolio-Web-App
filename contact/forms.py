from .models import CollaborationRequest
from django import forms


class CollaborationForm(forms.ModelForm):
    class Meta:
        model = CollaborationRequest
        fields = ('first_name', 'last_name', 'email', 'message')