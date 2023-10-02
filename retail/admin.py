from django.contrib import admin
from retail.models import Supplier, Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'country', 'city', 'street', 'house_number']
    list_filter = ['city']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'release_date', 'created_at']
    list_filter = ['name']
    search_fields = ['name']
