from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class CoreModelTest(TestCase):

	def test_new_user(self):
		"""Creating new user"""
		email = "test@wdev.com"
		password = "123456"
		user = get_user_model().objects.create_user(
			email=email,
			password=password
		)

		self.assertEqual(user.email, email)
		self.assertTrue(user.check_password(password))