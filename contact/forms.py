from .models import CollaborationRequest
from django.conf import settings
from django import forms


class CollaborationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = CollaborationRequest
        fields = ('first_name', 'last_name', 'email', 'message')

    def save(self, commit=True):
        instance = super().save(commit=False)
        current_consultant = settings.CONTEXT_CONFIG_DATA['CURRENT_CONSULTANT']
        instance.consultant_id_id = current_consultant  # Set the consultant_id
        if commit:
            instance.save()
        return instance
