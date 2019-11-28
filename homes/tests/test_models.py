from django.test import TestCase

from homes.models import Home
from django.contrib.auth.models import User


class TestModelHome(TestCase):
    
    def setUp(self):
        Home.objects.create(
            property_title='The Cliff',
            address='455 Paper Mill Road',
            city='Atlanta',
            state='GA',
            zipcode='30046',
            information='This is just a test, no worry, be happy',
            price=125000,
            bedrooms=2,
            bathrooms=1.5,
            garage=1,
            homesize=1111,
            landsize=2.1,
            is_posted=True
        )
    
    def test_check_items(self):
        home = Home()
        home.property_title = 'The Cliff'
        home.city = 'Atlanta'
        home.state = 'GA'
        home.zipcode = '30046'
        home.save()

        record = Home.get(pk=1)
        self.assertEqual(record, home)


    