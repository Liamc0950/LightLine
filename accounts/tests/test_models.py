from django.test import TestCase
from accounts.models import Profile
from django.utils import timezone
from accounts.forms import ProfileCreationForm
from django.contrib.auth.models import User

# models test
class UserTest(TestCase):

    def create_user(self, username='username', first_name='first_name', last_name='last_name',email='email'):
        return User.objects.create(
                                    username=username, 
                                    first_name=first_name,
                                    last_name=last_name, 
                                    email = email
                                    )
    def test_profile_creation(self):
        user = self.create_user()
        self.assertTrue(isinstance(user, User))
        # Check .__str__()
        self.assertEqual(user.profile.__str__(), user.username)
        # Check getName()
        self.assertEqual(user.profile.getName(), user.first_name + " " + user.last_name)
