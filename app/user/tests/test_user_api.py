from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')

def create_user(**params):
	return get_user_model().objects.create_user(**params)


class UserApiTests(TestCase):
	"""Test Users API"""
	def setUp(self):
		self.client = APIClient()
		
	def test_create_valid_user_success(self):
		"""Test Create User Success"""
		payload = {
			'email' : 'test@wdev.com',
			'password' : '123456',
			'username' : 'Test Dev'
		}

		res = self.client.post(CREATE_USER_URL, payload)

		self.assertEqual(res.status_code, status.HTTP_201_CREATED)
		user = get_user_model().objects.get(**res.data)

		self.assertTrue(user.check_password(payload["password"]))
		self.assertNotIn('password', res.data)

	def test_user_exists(self):
		"""Test Check User Email Exists"""
		payload = {
			'email' : 'test@wdev.com',
			'password' : '123456',
			'username' : "Test Dev 2"
		}

		create_user(**payload)
		res = self.client.post(CREATE_USER_URL, payload)
		self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


	def test_password_too_short(self):
		"""Test Check password len < 5"""
		payload = {
			'email' : 'test@wdev.com',
			'password' : '12',
		}
		res = self.client.post(CREATE_USER_URL, payload)

		self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
		user_exists = get_user_model().objects.filter(
			email=payload["email"]
		).exists()
		self.assertFalse(user_exists)