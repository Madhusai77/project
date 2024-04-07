# Inside referrals/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from .models import User

class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'password': 'test123',
            'referral_code': '123456'  # Assuming this is a valid referral code
        }
        
    def test_user_registration(self):
        response = self.client.post('/register/', self.user_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('user_id', response.data)
        self.assertIn('message', response.data)

