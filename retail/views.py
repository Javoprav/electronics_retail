from rest_framework import viewsets
from retail.models import Supplier, Product
from retail.serializers.serializers import SupplierSerializers, ProductSerializers


class SupplierViewSet(viewsets.ModelViewSet):
    """Реализация CRUD для Module с помощью viewsets"""
    serializer_class = SupplierSerializers
    queryset = Supplier.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    """Реализация CRUD для Module с помощью viewsets"""
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
