from .models import CollaborationRequest
from django.conf import settings
from django import forms


class CollaborationForm(forms.ModelForm):
    """
    CollaborationForm is a Django ModelForm for handling collaboration requests.

    Fields:
        first_name (CharField): The first name of the person making the request.
        last_name (CharField): The last name of the person making the request.
        email (EmailField): The email address of the person making the request.
        message (CharField): The message content of the collaboration request.

    Meta:
        model (CollaborationRequest): The model associated with this form.
        fields (tuple): The fields to include in the form.

    Methods:
        save(commit=True):
            Saves the form instance. Sets the consultant_id to the current consultant
            from the settings before saving. If commit is True, the instance is saved
            to the database.
    """
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
