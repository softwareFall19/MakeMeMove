from django.test import TestCase
from homes.models import Home

# Create your tests here.
class HomesTest(TestCase):

    # A simple test
    def test_homes_fields(self):
        home = Home()
        home.property_title = "Testing the titles"
        home.information = "What are the descriptions of the homes"

        record = Home.objects.get(pk=1)
        self.assertEqual(record, home)

    # def test_string_method(self):
    #     home = Home()
    #     home.property_title = "Bring on the tests"
    #     home.information = "What are the descriptions of the homes"

    #     self.assertEqual(home.__str__(), "Bring on the tests")

