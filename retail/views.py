from rest_framework import viewsets
from retail.models import Supplier, Product, Network
from retail.serializers.serializers import SupplierSerializers, ProductSerializers


class SupplierViewSet(viewsets.ModelViewSet):
    """Реализация CRUD для Supplier с помощью viewsets"""
    serializer_class = SupplierSerializers
    queryset = Supplier.objects.all()


class NetworkViewSet(viewsets.ModelViewSet):
    """Реализация CRUD для Supplier с помощью viewsets"""
    serializer_class = SupplierSerializers
    queryset = Network.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    """Реализация CRUD для Product с помощью viewsets"""
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
