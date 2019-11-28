from django.test import TestCase, Client

class TestAgentPage(TestCase):
    client = Client()

    def test_agent_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
