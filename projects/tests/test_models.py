from django.test import TestCase
from django.contrib.auth.models import User
from projects.models import Project

# test active Project
class ProjectTestActive(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'testpassword')
        self.project = Project.objects.create(showName='Test', showNameShort='T', venue='Test Venue', projectCreator=self.user.profile)
        self.project.active = True
        self.project.save()
    def test_ProjectActive(self):
        self.assertEqual(self.project.__str__(), self.project.showName)
        self.assertEqual(self.project.isActive(), True)

# test inactive Project
class ProjectTestInactive(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'testpassword')
        self.project = Project.objects.create(showName='Test', showNameShort='T', venue='Test Venue', projectCreator=self.user.profile)
        self.project.active = False
        self.project.save()
    def test_ProjectInActive(self):
        self.assertEqual(self.project.__str__(), self.project.showName)
        self.assertEqual(self.project.isActive(), False)
