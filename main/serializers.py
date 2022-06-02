from rest_framework import serializers

from .models import Product, Credit, Manufacturer, Contract


class CreditSerializer(serializers.ModelSerializer):
    """Кредитные заявки"""

    class Meta:
        model = Credit
        fields = ['id', 'date', 'contract']


class ContractSerializer(serializers.ModelSerializer):
    """Контракт"""

    class Meta:
        model = Contract
        fields = ['id', 'date']


class ProductSerializer(serializers.ModelSerializer):
    """Товар"""

    class Meta:
        model = Product
        fields = ['id', 'title', 'manufacturer', 'credit', 'date']


class ManufacturerSerializer(serializers.ModelSerializer):
    """Производитель"""

    class Meta:
        model = Manufacturer
        fields = ['id', 'title', 'date']
