from django.test import TestCase

from advertising.models import Advertise


class TestModelAdvertise(TestCase):

    def setUp(self):
        Advertise.objects.create(role='Homebuyer/seller', name='David')


    def test_name_and_role(self):
        role = Advertise.objects.get(role='Homebuyer/seller')
        name = Advertise.objects.get(name='David')
        self.assertTrue(role, 'Homebuyer/seller')
        self.assertTrue(name, 'David')

    def test_is_str_is_name(self):
        name = Advertise.objects.create(name='David')
        self.assertEqual(str(name), 'David')


