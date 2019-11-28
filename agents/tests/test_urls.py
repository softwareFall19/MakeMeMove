from django.test import TestCase
from django.urls import reverse, resolve
from agents.views import agents

class TestUrlsAgent(TestCase):


    # Which view django will call
    def test_agent_url_is_resolved(self):
        url = reverse('agents')
        print(resolve(url))
        self.assertEqual(resolve(url).func, agents)

    