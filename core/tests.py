from django.test import TestCase,SimpleTestCase


# Create your tests here.
class SimpleCase(SimpleTestCase):
    def test_home_states_code(self):
        respone= self.client.get('/')
        self.assertEqual(respone.status_code,200)
    
    def test_about_states_code(self):
        respone= self.client.get('/about/')
        self.assertEqual(respone.status_code,200)