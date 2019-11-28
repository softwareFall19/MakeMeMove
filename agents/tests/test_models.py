from django.test import TestCase

from agents.models import Agent


class TestModelAgent(TestCase):
    
    def setUp(self):
        Agent.objects.create(
            name='David',
            email='abc@yahoo.com',
            telephone='4045555555',
            information='This is just a test, no worry, be happy',
            # picture='static/img/two_meet.jpg'
        )

    def test_information_content(self):
        agent = Agent.objects.get(id=1)
        expected_obj_info = f'{agent.information}'
        self.assertEqual(expected_obj_info, 'This is just a test, no worry, be happy')

    def test_is_str_is_name(self):
        name = Agent.objects.create(name='David')
        self.assertEqual(str(name), 'David')

    # def test_agent_picture(self):
    #     agent = Agent.objects.get(id=1)
    #     self.assertIsNotNone(agent.picture)