from django.contrib import admin
from retail.models import Supplier, Product, Network


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'country', 'city', 'street', 'debt', 'house_number']
    list_filter = ['city']
    search_fields = ['name']
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        """Очищающий задолженность перед поставщиком у выбранных объектов"""
        queryset.update(debt=0)

    clear_debt.short_description = "Очистить задолженность"



@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'country', 'city', 'street', 'house_number', 'supplier']
    list_filter = ['city']
    search_fields = ['name']
    raw_id_fields = ['supplier']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'release_date', 'network', 'created_at']
    list_filter = ['name']
    search_fields = ['name']
    raw_id_fields = ['network']
