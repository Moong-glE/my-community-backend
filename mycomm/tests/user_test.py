from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from mycomm.models import User
from mycomm.serializers.user import UserSerializer, UserCreateSerializer


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username='test@example.com',
            password='test',
            email="test@example.com",
            student_id='12341234',
        )

    def test_sign_up(self):
        self.assertEqual(User.objects.count(), 1, "Success sign up")

    def test_sign_in(self):
        user = User.objects.get(id=1)

        self.assertEqual(user.username, 'test@example.com', "Success sign in")


class UserCreateSerializerTest(TestCase):
    def setUp(self):
        self.data = {
            'username': 'test@example.com',
            'password': 'test',
            'email': "test@example.com",
            'student_id': '12341234',
        }

        self.data2 = {
            'username': 'test2@example.com',
            'password': 'test',
            'email': "test2@example.com",
            'student_id': '12341234',
        }

    def test_sign_up(self):
        serializer = UserCreateSerializer(data=self.data)
        serializer.is_valid()
        serializer.create(self.data2)

        user = User.objects.get(username=self.data2['username'])

        self.assertEqual(self.data2['username'], user.username)


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username='test@example.com',
            password='test',
            email="test@example.com",
            student_id='12341234',
        )

    def test_sign_in(self):
        response = self.client.post(reverse('sign-in'),
                                    {'username': 'test@example.com', 'password': 'test'})
        user = User.objects.get(username='test@example.com')
        serializer = UserSerializer(user)

        user = response.data['user']
        self.assertEqual(user['username'], serializer.data['username'])


class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.data = {
            'username': 'test@example.com',
            'password': 'test',
            'email': "test@example.com",
            'student_id': '12341234',
        }

    def test_sign_up(self):
        response = self.client.post(reverse('sign-up'), self.data)

        user = User.objects.get(username='test@example.com')

        self.assertEqual(response.data['user']['username'], user.username)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
