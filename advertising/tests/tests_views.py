from django.test import TestCase, Client
from django.urls import reverse
from advertising.models import Advertise
import json



class TestViewsAdvertise(TestCase):

    def setUp(self):
        self.ad_1 = Advertise.objects.create(
            name='David',
            role='Homebuyer/seller'
        )


    def test_advertising_GET(self):
        client = Client()

        response = client.get(reverse('advertising'))
        # Are we accessing the content perfectly
        self.assertEqual(response.status_code, 200)
        # test for correct template
        self.assertTemplateUsed(response, 'advertising/advertising.html')

    def test_advertising_POST(self):
        client = Client()

        response = client.post('advertising/advertising.html', {'role': 'Homebuyer/seller', 'name': 'David', 'telephone': '4045555555', 'email': 'abc@yahoo.com'})
        self.assertEqual(response.status_code, 404)


