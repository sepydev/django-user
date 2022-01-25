from django.test import TestCase

from user.models import User


class UserModelTest(TestCase):

    def test_create_user(self):
        email = 'test@test.com'
        password = 'testpass'
        user = User.objects.create_user(email, password)
        added_user = User.objects.filter(pk=user.pk).first()
        self.assertEqual(email, added_user.email)
        self.assertTrue(user.check_password(password))

    def test_create_superuser(self):
        email = 'test@test.com'
        password = 'testpass'
        user = User.objects.create_superuser(email, password)
        added_user = User.objects.filter(pk=user.pk).first()
        self.assertEqual(email, added_user.email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(added_user.is_staff, 1)
        self.assertEqual(added_user.is_superuser, 1)
