from rest_framework.routers import DefaultRouter
from django.urls import path, include
from retail.views import SupplierViewSet, ProductViewSet, NetworkViewSet

router = DefaultRouter()
router.register(r'supplier', SupplierViewSet, basename='supplier')

router_network = DefaultRouter()
router_network.register(r'network', NetworkViewSet, basename='network')

router_product = DefaultRouter()
router_product.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router_network.urls)),
    path('', include(router_product.urls)),
]
