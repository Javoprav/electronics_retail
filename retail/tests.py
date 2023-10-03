from rest_framework.test import APITestCase
from rest_framework import status
from retail.models import Supplier, Product, Network
from users.models import User, UserRoles


class SupplierTestCase(APITestCase):
    """Тесты модели Supplier"""

    def setUp(self) -> None:
        """Подготовка данных перед каждым тестом"""
        self.user = User.objects.create(
            email='user@user1.com',
            is_staff=False,
            is_superuser=False,
            is_active=True,
            role=UserRoles.MEMBER,
        )
        self.user.set_password('123')
        self.user.save()
        response = self.client.post('/api/token/', {"email": "user@user1.com", "password": "123"})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_model_name = 'supplier_for_test'

    def test_supplier_create(self):
        """Тест создания модели Supplier"""
        response = self.client.post('/api/supplier/', {
            "name": "Леруа25",
            "email": "lerua25@gmail.com",
            "country": "Франция",
            "city": "Париж",
            "street": "Лягушачьих лапок",
            "house_number": "2",
            "debt": "22.00"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_supplier(self):
        """Тест деталей модели Supplier"""
        self.test_supplier_create()
        response = self.client.get(f'/api/supplier/1/')
        response2 = self.client.get('/api/supplier/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'id': 1, 'name': 'Леруа25', 'email': 'lerua25@gmail.com', 'country': 'Франция',
                          'city': 'Париж', 'street': 'Лягушачьих лапок', 'house_number': '2', 'debt': '22.00'})

    def test_list_supplier(self):
        """Тест списка модели Supplier"""
        self.test_supplier_create()
        response = self.client.get('/api/supplier/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         [{'id': 2, 'name': 'Леруа25', 'email': 'lerua25@gmail.com', 'country': 'Франция',
                           'city': 'Париж', 'street': 'Лягушачьих лапок', 'house_number': '2', 'debt': '22.00'}])
        self.assertEqual(Supplier.objects.all().count(), 1)

    def test_supplier_update_view(self):
        """Тест обновления модели Supplier"""
        self.moder = User.objects.create(
            email='moder@moder.com',
            is_staff=True,
            is_superuser=True,
            is_active=True,
            role=UserRoles.MODERATOR,
        )
        self.moder.set_password('123')
        self.moder.save()
        response_moder = self.client.post('/api/token/', {"email": "moder@moder.com", "password": "123"})
        self.access_token_moder = response_moder.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token_moder}')

        self.client.post('/api/supplier/', {
            "name": "Леруа25",
            "email": "lerua25@gmail.com",
            "country": "Франция",
            "city": "Париж",
            "street": "Лягушачьих лапок",
            "house_number": "2",
            "debt": "22.00"
        })

        response_update = self.client.patch('/api/supplier/5/', {
            "name": "Леруа",
            "email": "lerua@gmail.com",
            "country": "Франц",
            "city": "Париж",
            "street": "Лягушачьих лапок",
            "house_number": "2",
            "debt": "22.00"
        })
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)
        self.assertEqual(response_update.json()['name'], 'Леруа')

    def test_supplier_deletion(self):
        """Тест обновления модели Supplier"""
        self.test_supplier_create()
        response = self.client.delete('/api/supplier/4/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Supplier.objects.filter(id=1).exists())
