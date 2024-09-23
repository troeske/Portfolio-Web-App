from django.test import TestCase
from contact.forms import CollaborationForm

class CollaborationFormTest(TestCase):

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
            'last_name': 'D' * 201,   # Exceeding max_length of 200
            'email': 'jane.doe@example.com',
            'message': 'I would like to collaborate with you.'
        }
        form = CollaborationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)