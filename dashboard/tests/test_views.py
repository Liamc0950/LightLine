from django.test import TestCase
from accounts.models import Profile
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client
from django.contrib.auth import get_user_model



# Index View with user not logged in, should redirect to login page
class DashboardTestNoLogin(TestCase):

    def test_dashboard_index(self):
        url = reverse("dashboard:index")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 302)

# Index View with user logged in, should load dashboard index
class DashboardTestLogin(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'testpassword')

    def testLogin(self):
        self.client.login(username='test', password='testpassword')
        url = reverse("dashboard:index")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
