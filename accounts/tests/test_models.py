from django.test import TestCase
from accounts.models import Profile
from django.utils import timezone
from accounts.forms import ProfileCreationForm

# models test
class ProfileTest(TestCase):

    def create_profile(self, username='username', first_name='first_name', last_name='last_name',email='email'):
        return Profile.objects.create(
                                    username=username, 
                                    first_name=first_name,
                                    last_name=last_name, 
                                    email = email,
                                    created=timezone.now(),
                                    lastUpdate=timezone.now())

    def test_profile_creation(self):
        profile = self.create_profile()
        self.assertTrue(isinstance(profile, Profile))
        self.assertEqual(profile.__str__(), profile.username)
        self.assertEqual(profile.getName(), profile.first_name + " " + profile.last_name)
