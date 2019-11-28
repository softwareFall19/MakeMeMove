from django.test import TestCase
from django.urls import reverse, resolve
from webpages.views import index, about

class TestUrlsWebPages(TestCase):


    # Which view django will call
    def test_webpages_url_is_resolved(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEqual(resolve(url).func, index)

    def test_about_url_is_resolved(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEqual(resolve(url).func, about)