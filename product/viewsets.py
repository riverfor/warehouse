from rest_framework import viewsets, views

from product.models import AccountingModelProducts, StorageUnitsClass, StorageUnit
from .serializers import ProductSerializer, Product, AccountingModelSerializer, StorageUnitsClassSerializer, \
    StorageUnitSerializer


class AccountingModelViewset(viewsets.ModelViewSet):
    queryset = AccountingModelProducts.objects.all()
    serializer_class = AccountingModelSerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StorageUnitsClassViewset(viewsets.ModelViewSet):
    queryset = StorageUnitsClass.objects.all()
    serializer_class = StorageUnitsClassSerializer


class StorageUnitViewset(viewsets.ModelViewSet):

    queryset = StorageUnit.objects.all()
    serializer_class = StorageUnitSerializer

