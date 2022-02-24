import json

from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

UserModel = get_user_model()


def create_user_helper(
        email='test@test.com',
        password='p@123456'
):
    user = UserModel.objects.create_user(email, password)
    return user


def create_user_verify_and_login(
        client,
        email='test@test.com',
        password='p@123456'
):
    create_user(client, email, password)
    verify_email(email)
    return login(client, email, password)


def create_user(client, email, password):
    return client.post(
        '/accounts/api/registration/',
        {
            "username": email,
            "email": email,
            "password1": password,
            "password2": password
        }
    )


def verify_email(email):
    EmailAddress.objects.filter(email=email).update(verified=True)


def login(client, email, password):
    response = client.post(
        '/accounts/api/login/',
        {
            "username": email,
            "email": email,
            "password": password,
        }
    )
    return 'token ' + json.loads(response.content)['key']


class TestUserAPI(APITestCase):
    def test_create_user(self):
        response = create_user(self.client,
                               email='test@test.com',
                               password='p@123456')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_verify(self):
        email = 'test@test.com'
        create_user(self.client,
                    email=email,
                    password='p@123456')
        verify_email(email)
        verified_count = EmailAddress.objects.filter(email=email, verified=True).count()
        self.assertEqual(verified_count, 1)

    def test_login(self):
        email = 'test@test.com'
        password = 'p@123456'
        create_user(self.client,
                    email=email,
                    password=password)
        verify_email(email)
        token = login(self.client, email, password)
        self.assertTrue(token.__contains__('token '))
