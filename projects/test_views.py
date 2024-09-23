from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Project, Client
from home.models import Consultant
from portfolio.utils import get_consultant


class TestProjectDetailViewApproved(TestCase):

    def setUp(self):
        # we currnetly only supporting 1 consultant
        # consultant_id = get_consultant(True)
 
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
        
        self.project = Project(title="Project title", consultant_id=self.consultant,
                         slug="project-title", summary="Project summary",
                         link="https://www.example.com", customer="Project customer", confidential=True)
        
        self.project.save()

    def test_render_confidential_projects(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse('projects_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Project title", response.content)
        self.assertIn(b"Project summary", response.content)
        self.assertIn(b"https://www.example.com", response.content)
        self.assertIn(b"Project customer", response.content)

       