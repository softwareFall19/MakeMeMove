from django.test import TestCase
from django.urls import reverse, resolve
from contacts.views import info

class TestUrlsContact(TestCase):


    # Which view django will call
    def test_contact_url_is_resolved(self):
        url = reverse('info')
        print(resolve(url))
        self.assertEqual(resolve(url).func, info)