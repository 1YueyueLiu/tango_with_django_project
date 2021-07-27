from django.test import TestCase
from django.test import SimpleTestCase
# Create your tests here.

class SimpleTEsts(SimpleTestCase):
    def test1(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)