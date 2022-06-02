from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Credit, Contract, Product, Manufacturer
from .serializers import CreditSerializer, ContractSerializer, ProductSerializer, ManufacturerSerializer


class CreditViewSet(viewsets.ModelViewSet):
    """API для заявок"""
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)



class ContractViewSet(viewsets.ModelViewSet):
    """API для контрактов"""
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProductViewSet(viewsets.ModelViewSet):
    """API для товаров"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)


class ManufacturerViewSet(viewsets.ModelViewSet):
    """API для производителей"""
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

