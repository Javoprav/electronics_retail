from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User, UserRoles


class SuperUserTestCase(APITestCase):
    """Тест суперпользователя"""

    def setUp(self) -> None:
        """Подготовка данных перед тестом"""
        self.superuser = User.objects.create(
            id=3,
            email='superuser@user.com',
            is_staff=False,
            is_superuser=True,
            is_active=True,
            role=UserRoles.MEMBER
        )
        self.test_user = User.objects.create(
            id=5,
            email='user5@user.com',
            is_staff=False,
            is_superuser=False,
            is_active=True,
            role=UserRoles.MEMBER
        )
        self.superuser.set_password('123')
        self.superuser.save()
        response = self.client.post('/api/token/', {"email": "superuser@user.com", "password": "123"})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_super_user_get(self):
        """Тест суперюзера"""
        response = self.client.get('/users/3/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], 'superuser@user.com')

    def test_update_super_user(self):
        """Тест изменения пользователя суперюзером"""
        response = self.client.patch('/user/5/update/', {"city": 'Moscow'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['city'], 'Moscow')


class UserTestCase(APITestCase):
    """Тест пользователя"""

    def setUp(self) -> None:
        """Подготовка данных перед тестом"""
        self.test_user = User.objects.create(
            id=4,
            email='user@user.com',
            is_staff=False,
            is_superuser=False,
            is_active=True,
            role=UserRoles.MEMBER
        )
        self.test_user.set_password('123')
        self.test_user.save()
        response = self.client.post('/api/token/', {"email": "user@user.com", "password": "123"})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_users_get(self):
        """Тест пользователя"""
        response = self.client.get('/users/4/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], 'user@user.com')

    def test_update_user(self):
        """Тест изменения пользователя"""
        response = self.client.patch('/user/4/update/', {"city": 'Moscow'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['city'], 'Moscow')
