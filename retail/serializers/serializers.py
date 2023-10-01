from rest_framework import serializers
from retail.models import Supplier, Product


class SupplierSerializers(serializers.ModelSerializer):
    """Сериализатор для модели Supplier"""
    class Meta:
        model = Supplier
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):
    """Сериализатор для модели Product"""
    class Meta:
        model = Product
        fields = "__all__"
