from django.test import TestCase, Client

class TestHomePage(TestCase):
    client = Client()

    def test_webpage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 404)

