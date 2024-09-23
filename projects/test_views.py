from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from unittest.mock import patch, MagicMock
from .models import Project, Client
from home.models import Consultant


class TestProjectsListView(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="testuser", 
            password="password123"
        )

        self.consultant = Consultant.objects.create(
            consultant_id=1,
            first_name="Test",
            last_name="Consultant",
            email="test@test.com"
        )

        self.client_instance = Client.objects.create(
            client = self.user,
            approved=True,
            allow_delete=True,
            consultant = self.consultant,
            email="test@test.com"
        )
        
        self.project = Project(title="Project title", 
                            consultant_id=self.consultant,
                            slug="project-title", 
                            sub_heading="super project",
                            customer="Project customer", 
                            confidential=True,
                            )
        
        self.project.save()


    @patch('projects.views.get_consultant')
    @patch('projects.views.client_approved')
    def test_render_confidential_projects(self, mock_client_approved, mock_get_consultant):
        mock_get_consultant.return_value = self.consultant.consultant_id
        mock_client_approved.return_value = self.client_instance.approved
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse('projects_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Project title", response.content)
        self.assertIn(b"super project", response.content)

    @patch('projects.views.get_consultant')
    @patch('projects.views.client_approved')
    def test_dont_render_confidential_projects(self, mock_client_approved, mock_get_consultant):
        mock_get_consultant.return_value = self.consultant.consultant_id
        mock_client_approved.return_value = False
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse('projects_list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"Project title", response.content)

       