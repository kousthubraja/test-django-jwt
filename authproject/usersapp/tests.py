from django.test import TestCase, Client
from django.contrib.auth.models import User
import json
from .models import UserProfile


class JWTAuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass123')
        self.user_profile = UserProfile.objects.create(
            user=self.user, first_name='Test', last_name='User')

    def test_valid_user_login(self):
        response = self.client.post(
            '/usersapp/login', {'username': 'testuser', 'password': 'testpass123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)

        # Store the token for further tests
        self.access_token = response.data['access']

    def test_invalid_user_login(self):
        response = self.client.post(
            '/usersapp/login', {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 401)
        self.assertIn('error', response.data)

    def test_user_profile_authenticated(self):
        # Ensure the token has been generated before this test
        if not hasattr(self, 'access_token'):
            self.test_valid_user_login()

        response = self.client.get(
            '/usersapp/profile', HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        self.assertEqual(response.status_code, 200)
        self.assertIn('first_name', response.data)
        self.assertIn('last_name', response.data)
        self.assertEqual(response.data['first_name'], 'Test')
        self.assertEqual(response.data['last_name'], 'User')
