from django.urls import path, include, re_path
from rest_framework import routers

from .viewsAPI import CreditViewSet, ContractViewSet, ProductViewSet, ManufacturerViewSet

router = routers.DefaultRouter()
router.register(r'credit', CreditViewSet)
router.register(r'contract', ContractViewSet)
router.register(r'product', ProductViewSet)
router.register(r'manufacturer', ManufacturerViewSet)

urlpatterns = [
    path('drf-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),


]
