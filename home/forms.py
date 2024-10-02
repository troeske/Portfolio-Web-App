from allauth.account.forms import SignupForm
from django import forms
from collections import OrderedDict
from django.core.mail import send_mail
from django.conf import settings


class CustomSignupForm(SignupForm):
    """
    CustomSignupForm extends the default SignupForm to include additional
    fields for first name and last name, and modifies the email field to
    be required.

    Suggested by github copilot.

    Attributes:
        first_name (forms.CharField): A form field for the user's first name.
        last_name (forms.CharField): A form field for the user's last name.
        email (forms.EmailField): A form field for the user's email, set
        as required.

    Methods:
        __init__(self, *args, **kwargs): Initializes the form and updates
        field labels and placeholders.
        save(self, request): Saves the user instance with additional first name
                             and last name fields, and sends an
                             email notification to the consultant.
    """
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    email = forms.EmailField(required=True, label='Your Email')

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Your Email'
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['first_name'].label = 'First Name'
        self.fields['first_name'].widget.attrs.update(
                {'placeholder': 'First Name'})
        self.fields['last_name'].label = 'Last Name'
        self.fields['last_name'].widget.attrs.update(
                {'placeholder': 'Last Name'})
        self.fields['password1'].label = 'Password'
        self.fields['password1'].widget.attrs.update(
                {'placeholder': 'Password'})
        self.fields['password2'].label = 'Password Confirmation'
        self.fields['password2'].widget.attrs.update(
                {'placeholder': 'Password Confirmation'})

        self.fields = OrderedDict([
            ('username', self.fields['username']),
            ('first_name', self.fields['first_name']),
            ('last_name', self.fields['last_name']),
            ('email', self.fields['email']),
            ('password1', self.fields['password1']),
            ('password2', self.fields['password2']),
        ])

    def save(self, request):
        """
        Saves the user information and sends a notification email to
        the consultant.

        Args:
            request: The HTTP request object containing the form data.

        Returns:
            user: The saved user instance with updated first/last name.

        This method performs the following actions:
        1. Saves the user instance using the parent class's save method.
        2. Updates the user's first name and last name with the cleaned
           data from the form.
        3. Sends an email notification to the consultant with the
           new registration details.
        """
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        # Send email to consultant
        consultant_message = (
            f"Hi {settings.CONTEXT_CONFIG_DATA['consultant_fname']}!\n\n"
            "You have a new registration request:\n\n"
            "----------------------\n"
            f"Name (last, first): {user.last_name}, {user.first_name}\n"
            "----------------------\n"
            f"eMail: {user.email}\n"
            "----------------------\n"

            "\nYour friendly Portfolio App django"
        )
        subject = '[NO-REPLY] you have new registration'
        send_mail(
            subject,
            consultant_message,
            "",
            [settings.CONTEXT_CONFIG_DATA['consultant_email']]
            )

        return user
