from rest_framework import viewsets
from retail.models import Supplier, Product, Network
from retail.permissions import IsActive
from retail.serializers.serializers import SupplierSerializers, ProductSerializers, NetworkSerializers
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class SupplierViewSet(viewsets.ModelViewSet):
    """Реализация CRUD для Supplier с помощью viewsets"""
    serializer_class = SupplierSerializers
    queryset = Supplier.objects.all()
    filter_backends = [SearchFilter]
    filterset_fields = ['country']
    permission_classes = [IsAuthenticated, IsActive]

    def update(self, request, *args, **kwargs):
        """Делает невозможным изменение поля debt"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        if 'debt' in serializer.validated_data:
            serializer.validated_data.pop('debt')

        self.perform_update(serializer)

        return Response(serializer.data)


class NetworkViewSet(viewsets.ModelViewSet):
    """Реализация CRUD для Network с помощью viewsets"""
    serializer_class = NetworkSerializers
    queryset = Network.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductViewSet(viewsets.ModelViewSet):
    """Реализация CRUD для Product с помощью viewsets"""
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsActive]
