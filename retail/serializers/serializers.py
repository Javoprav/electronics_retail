from rest_framework import serializers
from retail.models import Supplier, Product, Network


class SupplierSerializers(serializers.ModelSerializer):
    """Сериализатор для модели Supplier"""
    class Meta:
        model = Supplier
        fields = "__all__"


class NetworkSerializers(serializers.ModelSerializer):
    """Сериализатор для модели Network"""
    class Meta:
        model = Network
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):
    """Сериализатор для модели Product"""
    class Meta:
        model = Product
        fields = "__all__"
