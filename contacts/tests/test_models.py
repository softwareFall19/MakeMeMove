from django.test import TestCase

from contacts.models import Contact


class TestModelContact(TestCase):
    
    def setUp(self):
        self.contact1 = Contact.objects.create(
            name='David',
            email='abc@yahoo.com',
            phone='4045555555',
            message='This is just a test, no worry, be happy',
            home_id=24,
            user_id=2          
        )

    def test_create_contact(self):
        contact = self.contact1
        self.assertTrue(isinstance(contact, Contact))
        
    def test_is_str_is_name(self):
        name = Contact.objects.create(name='David')
        self.assertEqual(str(name), 'David')