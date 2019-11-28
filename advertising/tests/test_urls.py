from django.test import TestCase
from django.urls import reverse, resolve
from advertising.views import advertising

class TestUrlsAdvertise(TestCase):


    # Which view django will call
    def test_advertising_url_is_resolved(self):
        url = reverse('advertising')
        print(resolve(url))
        self.assertEqual(resolve(url).func, advertising)