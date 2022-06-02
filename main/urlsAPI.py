from django.urls import path, include
from rest_framework import routers

from .viewsAPI import CreditViewSet, ContractViewSet, ProductViewSet, ManufacturerViewSet

router = routers.DefaultRouter()
router.register(r'credit', CreditViewSet)
router.register(r'contract', ContractViewSet)
router.register(r'product', ProductViewSet)
router.register(r'manufacturer', ManufacturerViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),


]
