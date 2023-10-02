from django.contrib import admin
from retail.models import Supplier, Product, Network


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'country', 'city', 'street', 'house_number']
    list_filter = ['city']
    search_fields = ['name']


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'country', 'city', 'street', 'house_number', 'supplier']
    list_filter = ['city']
    search_fields = ['name']
    raw_id_fields = ['supplier']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'release_date', 'network', 'debt', 'created_at']
    list_filter = ['name']
    search_fields = ['name']
    raw_id_fields = ['network']