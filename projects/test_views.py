from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase, Client as TestClient
from unittest.mock import patch
from .models import Project, Client
from home.models import Consultant


class TestProjectsListView(TestCase):
    """Testing thje projects list view
        
    """
    
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


    @patch.dict('django.conf.settings.CONTEXT_CONFIG_DATA', {'CURRENT_CONSULTANT': 1})
    @patch('projects.views.client_approved')
    def test_render_confidential_projects(self, mock_client_approved):
        mock_client_approved.return_value = self.client_instance.approved
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse('projects_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Project title", response.content)
        self.assertIn(b"super project", response.content)

    @patch.dict('django.conf.settings.CONTEXT_CONFIG_DATA', {'CURRENT_CONSULTANT': 1})
    @patch('projects.views.client_approved')
    def test_dont_render_confidential_projects(self, mock_client_approved):
        mock_client_approved.return_value = False
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse('projects_list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"Project title", response.content)


class TestClientDeleteView(TestCase):
    """Testing the client delete view
        
    """
    
    def setUp(self):
        self.test_client = TestClient()
        self.superuser = User.objects.create_superuser(
            username='superuser', 
            password='password123', 
            email='superuser@test.com'
        )
        self.normal_user = User.objects.create_user(
            username='normaluser', 
            password='password123', 
            email='normaluser@test.com'
        )
    
    def test_superuser_can_delete_client(self):
        self.test_client.login(username='superuser', password='password123')
        response = self.test_client.post(reverse('client_delete', args=['normaluser']))
        self.assertFalse(User.objects.filter(username='normaluser').exists())

    def test_non_superuser_cannot_delete_client(self):
        self.test_client.login(username='normaluser', password='password123')
        response = self.test_client.post(reverse('client_delete', args=['superuser']))
        self.assertTrue(User.objects.filter(username='superuser').exists())


class TestApproveClientView(TestCase):
    """Testing the approve client view
        
    """
    
    def setUp(self):
        self.test_client = TestClient()
        self.superuser = User.objects.create_superuser(
            username='superuser', 
            password='password123',
            email='superuser@test.com'
        )

        self.normal_user = User.objects.create_user(
            username='normaluser', 
            password='password123',
            email='normaluser@test.com'
        )

        self.consultant = Consultant.objects.create(
            consultant_id=1,
            first_name="Test",
            last_name="Consultant",
            email="test@test.com"
        )

        self.client_instance = Client.objects.create(
            client = self.normal_user,
            approved=False,
            allow_delete=True,
            consultant = self.consultant,
            email="test@test.com"
        )
    
    @patch('home.middleware.Config.objects.get')
    def test_superuser_can_approve_client(self, mock_get_config):
        mock_get_config.return_value.value = self.consultant.consultant_id
        self.test_client.login(username='superuser', password='password123')
        response = self.test_client.post(reverse('approve_client', args=[self.client_instance.id]))
        self.assertTrue(Client.objects.get(client=self.normal_user).approved)
    
    @patch('home.middleware.Config.objects.get')
    def test_normaluser_cannot_approve_client(self, mock_get_config):
        mock_get_config.return_value.value = self.consultant.consultant_id
        self.test_client.login(username='normaluser', password='password123')
        response = self.test_client.post(reverse('approve_client', args=[self.client_instance.id]))
        self.assertFalse(Client.objects.get(client=self.normal_user).approved)