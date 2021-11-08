from django.test import TestCase
from django.contrib.auth import get_user_model
from dap.models import Reg_User as ru

import unittest
from unittest.mock import patch, call
from sending_mail_by_python import sending_mail as target


class UsersManagersTests(TestCase):
	def test_create_user(self):
		User = get_user_model()
		user = User.objects.create_user(email = 'kiosk@user.com', password="foo")
		self.assertEqual(user.email, 'kiosk@user.com')
		self.assertTrue(user.is_active)
		self.assertFalse(user.is_staff)
		self.assertFalse(user.is_superuser)

		try:
			self.assertIsNone(user.username)
		except AttributeError:
			pass 
		with self.assertRaises(TypeError):
			User.objects.create_user()

		with self.assertRaises(TypeError):
			User.objects.create_user(email='')

		with self.assertRaises(ValueError):
			User.objects.create_user(email='', password='foo')


	def test_create_superuser(self):
		User = get_user_model()
		admin_user = User.objects.create_superuser(email='kiosk@admin.com', password='foo')
		self.assertEqual(admin_user.email, 'kiosk@admin.com')
		self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)



class UserLogiinTests(TestCase):
	def test_reg_users(self):
		user = ru.objects.create_user(email = 'kiosk@user.com', password="abracadabra")
		self.assertEqual(user.email, 'kiosk@user.com')
		self.assertTrue(user.is_active)

		try:
			self.assertIsNone(user.username)
		except AttributeError:
			pass

class SendEmailTests(unittest.TestCase):
    def test_send_email(self):
        with patch("smtplib.SMTP") as smtp:
            from_address = "from@domain.com"
            to_address = ["to@domain.com"]

            msg = target.build_email(
                from_address, to_address, "subject", "message")
            target.send_email(msg)

            # Get instance of mocked SMTP object
            instance = smtp.return_value