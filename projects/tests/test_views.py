from django.test import TestCase
from accounts.models import Profile
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client
from django.contrib.auth import get_user_model
from projects.models import Project
from http import HTTPStatus


# projectIndex View with user not logged in, should redirect to login page
class ProjectIndexTestNoLogin(TestCase):

    def test_dashboard_index(self):
        url = reverse("projects:projectIndex")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 302)

# projectIndex View with user logged in, should load dashboard index
class ProjectIndexTestLogin(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'testpassword')
        project = Project.objects.create(showName='Test', showNameShort='T', venue='Test Venue', projectCreator=self.user.profile)
        project.active = True
        project.save()

    def test_Login(self):
        self.client.login(username='test', password='testpassword')
        url = reverse("projects:projectIndex")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

class ProjectCreateTestNoLogin(TestCase):

    def test_get(self):
        url = reverse("projects:projectCreate")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 302)

# Index View with user logged in, should load dashboard index
class ProjectCreateTestLogin(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'testpassword')
        project = Project.objects.create(showName='Test', showNameShort='T', venue='Test Venue', projectCreator=self.user.profile)
        project.active = True
        project.save()

    def test_get(self):
        self.client.login(username='test', password='testpassword')
        url = reverse("projects:projectCreate")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_create_success(self):
        response = self.client.post("/projects/projectCreate", data={"showName": "Test Show", "showNameShort" : "TS", "venue" : "Test Venue"})

        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        userProjects = Project.objects.filter(projectCreator= self.user.profile, active=True) 

        for project in userProjects:
            self.assertEqual(project.isActive(), False)

