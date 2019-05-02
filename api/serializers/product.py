from rest_framework import serializers

from base.serializers import AbstractSerializer, LoggerSerializer
from product.models import *


class ContainerClassSerializer(LoggerSerializer, AbstractSerializer):

    class Meta:
        model = ContainerParams
        fields = (
            'id',
            'name',
            'cont_width',
            'cont_height',
            'cont_length',
        ) + AbstractSerializer.Meta.fields


class ProductModelSerializer(LoggerSerializer, AbstractSerializer):

    class Meta:
        model = AccountingModelProducts
        fields = (
            'id',
            'name',
            'use_date',
            'use_serial',
            'use_parts',
        ) + AbstractSerializer.Meta.fields


class ProductListSerializer(LoggerSerializer, AbstractSerializer):
    model = ProductModelSerializer(read_only=True)
    base_cont_type = ContainerClassSerializer(read_only=True)
    units = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='unit-detail')

    class Meta:
        model = Product
        fields = (
            'id',
            'vendor',
            'name',
            'description',
            'model',
            'base_cont_type',
            'units',
        ) + AbstractSerializer.Meta.fields


class ProductSerializer(LoggerSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'vendor',
            'name',
            'description',
            'model',
            'base_cont_type',
        )


class UnitClassSerializer(LoggerSerializer, AbstractSerializer):

    class Meta:
        model = StorageUnitsClass
        fields = (
            'id',
            'name',
        ) + AbstractSerializer.Meta.fields


class UnitListSerializer(LoggerSerializer, AbstractSerializer):
    unit_class = UnitClassSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = StorageUnit
        fields = (
            'id',
            'product',
            'ratio',
            'unit_class',
            'unit_width',
            'unit_height',
            'unit_length',
        ) + AbstractSerializer.Meta.fields


class UnitSerializer(LoggerSerializer, AbstractSerializer):

    class Meta:
        model = StorageUnit
        fields = (
            'id',
            'product',
            'ratio',
            'unit_class',
            'unit_width',
            'unit_height',
            'unit_length',
        ) + AbstractSerializer.Meta.fields


class UnitEditSerializer(LoggerSerializer):

    class Meta:
        model = StorageUnit
        fields = (
            'id',
            'ratio',
            'unit_class',
            'unit_width',
            'unit_height',
            'unit_length',
        )