from rest_framework.routers import DefaultRouter
from django.urls import path, include
from retail.views import SupplierViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'edu_modules', SupplierViewSet, basename='edu_modules')

router_product = DefaultRouter()
router_product.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router_product.urls)),
]
