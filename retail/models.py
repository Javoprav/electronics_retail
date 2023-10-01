from django.db import models


class Supplier(models.Model):
    """Модель описывающая Поставщика с установкой звеньев"""

    LEVEL_CHOICES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель')
    )

    name = models.CharField(max_length=100, verbose_name='название')
    email = models.EmailField(unique=True, verbose_name='почта')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    house_number = models.CharField(max_length=100, verbose_name='номер дома')
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='задолженность')
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='звено')

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель описывающая продукт"""
    name = models.CharField(max_length=100, verbose_name='название')
    model = models.CharField(max_length=100, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='звено')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
