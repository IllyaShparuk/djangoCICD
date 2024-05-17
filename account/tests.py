from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class AuthViewsTestCase(TestCase):

    def test_sign_up_view_get(self):
        response = self.client.get(reverse('sign_up'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/sign_up.html')
        self.assertIn('form', response.context)

    def test_sign_up_view_post_valid(self):
        response = self.client.post(reverse('sign_up'), {
            'username': 'newuser',
            'password1': 'complex_password123',
            'password2': 'complex_password123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_sign_up_view_post_invalid(self):
        response = self.client.post(reverse('sign_up'), {
            'username': 'newuser',
            'password1': 'complex_password123',
            'password2': 'different_password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/sign_up.html')
        self.assertIn('form', response.context)
        self.assertFalse(User.objects.filter(username='newuser').exists())

    def test_user_logout_view(self):
        user = get_user_model().objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('user_logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertNotIn('_auth_user_id', self.client.session)

