from django.test import TestCase

from django.urls import reverse

# views test
class LandingTest(TestCase):

    def test_landing_index(self):
        url = reverse("landing:index")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

