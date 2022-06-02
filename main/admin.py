from django.contrib import admin

from .models import Credit, Contract, Product, Manufacturer


@admin.register(Credit)
class CreditApplicationAdmin(admin.ModelAdmin):
    """Кредитная заявка"""
    list_display = ('id', 'contract', 'date')
    list_display_links = ('contract',)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    """Контракт"""
    list_display = ('id', 'date')
    list_display_links = ('id',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Товар"""
    list_display = ('id', 'title', 'manufacturer', 'credit', 'date')
    list_display_links = ('title',)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    """Производитель"""
    list_display = ('id', 'title', 'date')
    list_display_links = ('title',)
