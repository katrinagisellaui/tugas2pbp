from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client

client = Client()


def test_create(self):
    """Test the url for "create"
    """

    response = self.client.get('/mywatchlist/html/{0}/'.format(self.userName))
    self.assertEqual(response.status_code, 200)