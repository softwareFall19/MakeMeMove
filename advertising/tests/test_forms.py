from django.test import TestCase

from advertising.forms import AdvertiseForm


class TestFormAdvertise(TestCase):

    def test_advertise_form_valid_data(self):
        form = AdvertiseForm(data={
            'role': 'Homebuyer/seller',
            'name': 'David',
            'email': 'abc@yahoo.com',
            'telephone': '4045555555'
        })
        self.assertTrue(form.is_valid())

    def test_advertise_form_invalid(self):
        form = AdvertiseForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)
