from rest_framework import serializers
from product.models import *


class ContainerClassSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='container_class-detail')

    class Meta:
        model = ContainerParams
        fields = (
            'url',
            'name',
            'cont_width',
            'cont_height',
            'cont_length',
        )


class ProductModelSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='product_model-detail')

    class Meta:
        model = AccountingModelProducts
        fields = (
            'url',
            'name',
            'use_date',
            'use_serial',
            'use_parts',
        )


class ProductListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail')
    model = ProductModelSerializer(read_only=True)
    base_cont_type = ContainerClassSerializer(read_only=True)
    units = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='unit-detail')

    class Meta:
        model = Product
        fields = (
            'url',
            'vendor',
            'name',
            'description',
            'model',
            'base_cont_type',
            'units',
        )


class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail')

    class Meta:
        model = Product
        fields = (
            'url',
            'vendor',
            'name',
            'description',
            'model',
            'base_cont_type',
        )


class UnitClassSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='unit_class-detail')

    class Meta:
        model = StorageUnitsClass
        fields = (
            'url',
            'name',
        )


class UnitListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='unit-detail')
    unit_class = UnitClassSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

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


class UnitSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='unit-detail')

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


class UnitEditSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='unit-detail')

    class Meta:
        model = StorageUnit
        fields = (
            'url',
            'ratio',
            'unit_class',
            'unit_width',
            'unit_height',
            'unit_length',
        )