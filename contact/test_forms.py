from django.test import TestCase
from contact.forms import CollaborationForm
from django.conf import settings
from home.models import Consultant
from django.urls import reverse
from django.core import mail
from .models import CollaborationRequest
from unittest.mock import patch

class CollaborationFormTest(TestCase):
    
    def setUp(self):
        # Create a Consultant instance to be referenced by the form
        self.consultant = Consultant.objects.create(
            consultant_id=1,
            first_name="Test",
            last_name="Consultant",
            email="test@test.com"
        )
        settings.CONTEXT_CONFIG_DATA = {'CURRENT_CONSULTANT': self.consultant.pk}
        
    def test_form_valid(self):
        form_data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'jane.doe@example.com',
            'message': 'I would like to collaborate with you.'
        }
        form = CollaborationForm(data=form_data)
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_form_invalid_missing_fields(self):
        form_data = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'message': ''
        }
        form = CollaborationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('message', form.errors)

    def test_form_invalid_email(self):
        form_data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'invalid-email',
            'message': 'I would like to collaborate with you.'
        }
        form = CollaborationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_form_max_length(self):
        form_data = {
            'first_name': 'J' * 201,  # Exceeding max_length of 200
            'last_name': 'D' * 201,   
            'email': 'jane.doe@example.com',
            'message': 'I would like to collaborate with you.'
        }
        form = CollaborationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        
    def test_collaboration_form_save(self):
        
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'message': 'I would like to collaborate on a project.',
        }
        form = CollaborationForm(data=form_data)
        self.assertTrue(form.is_valid())
        
        collaboration_request = form.save()
        self.assertEqual(collaboration_request.consultant_id_id, 1)
        self.assertEqual(collaboration_request.first_name, 'John')


class CollaborationFormSubmissionTests(TestCase):
    """
    unnittest for the collaboration form submission (post request)
    """
    def setUp(self):
        # Create a Consultant instance to be referenced by the form
        self.consultant = Consultant.objects.create(
            consultant_id=1,
            first_name="Test",
            last_name="Consultant",
            email="test@test.com"
        )
        settings.CONTEXT_CONFIG_DATA = {
            'CURRENT_CONSULTANT': self.consultant.pk,
            'consultant_fname': self.consultant.first_name,
            'consultant_lname': self.consultant.last_name,
            'consultant_email': self.consultant.email,
        }
    
    @patch('contact.views.send_mail')  # Mock send_mail to prevent actual email sending
    def test_successful_collaboration_form_submission(self, mock_send_mail):
        # let's provide all form data for submission
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'message': 'I would like to collaborate on a project.',
        }

        response = self.client.post(reverse('contact'), data=form_data)
        
        # first, let's check if the response is a redirect
        self.assertEqual(response.status_code, 200)
        
        # now, let's verify the CollaborationRequest is in the database
        collaboration_request = CollaborationRequest.objects.get(email='johndoe@example.com')
        self.assertIsNotNone(collaboration_request)
        self.assertEqual(collaboration_request.first_name, 'John')
        self.assertEqual(collaboration_request.consultant_id_id, self.consultant.pk)

        # Check that two emails were sent (one to the client and one to the consultant)
        self.assertEqual(mock_send_mail.call_count, 2)
        
        # Verify the first email content (to the client)
        client_email_args = mock_send_mail.call_args_list[0][0]
        self.assertIn('Hi John', client_email_args[1])  # client_message
        self.assertIn('Collaboration Request received', client_email_args[0])  # subject
        self.assertIn('johndoe@example.com', client_email_args[3])  # recipient

        # Verify the second email content (to the consultant)
        consultant_email_args = mock_send_mail.call_args_list[1][0]
        self.assertIn('Hi Test', consultant_email_args[1])  # consultant_message
        self.assertIn('you have a Collaboration Request', consultant_email_args[0])  # subject
        self.assertIn(self.consultant.email, consultant_email_args[3])  # recipient