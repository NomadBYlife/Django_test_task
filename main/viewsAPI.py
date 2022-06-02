from rest_framework import viewsets

from .models import Credit, Contract, Product, Manufacturer
from .serializers import CreditSerializer, ContractSerializer, ProductSerializer, ManufacturerSerializer


class CreditViewSet(viewsets.ModelViewSet):
    """API для заявок"""
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer


class ContractViewSet(viewsets.ModelViewSet):
    """API для контрактов"""
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """API для товаров"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    """API для производителей"""
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
