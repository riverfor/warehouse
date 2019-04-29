from .models import Product, AccountingModelProducts, StorageUnitsClass, StorageUnit
from rest_framework import serializers


class AccountingModelSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='accounting_model-detail')

    class Meta:
        model = AccountingModelProducts
        fields = (
            'url',
            'name',
            'use_date',
            'use_serial',
            'use_parts',
        )


class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail')
    model = AccountingModelSerializer(read_only=True)

    class Meta:
        model = Product
        fields = (
            'url',
            'vendor',
            'name',
            'model',
            'description',
        )


class StorageUnitsClassSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='unit_class-detail')

    class Meta:
        model = StorageUnitsClass
        fields = (
            'url',
            'name',

        )


class StorageUnitSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='unit-detail')
    product = ProductSerializer(read_only=True)
    unit_class = StorageUnitsClassSerializer(read_only=True)

    class Meta:
        model = StorageUnit
        fields = (
            'url',
            'product',
            'ratio',
            'unit_class',
            'unit_width',
            'unit_height',
            'unit_length',
        )
