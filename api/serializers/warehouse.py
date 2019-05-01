from rest_framework import serializers
from base.serializers import AbstractSerializer, LoggerSerializer
from warehouse.models import Warehouse, Rack, WarehouseCell


class RackListSerializer(LoggerSerializer, AbstractSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='rack-detail')

    class Meta:
        model = Rack
        fields = (
            'url',
            'name',
        ) + AbstractSerializer.Meta.fields


class CellSerializer(LoggerSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='cell-detail')

    class Meta:
        model = WarehouseCell
        fields = (
            'url',
            'rack',
            'tier',
            'position',
            'cell_width',
            'cell_height',
            'cell_length',

        )


class CellListSerializer(LoggerSerializer, AbstractSerializer):
    rack = RackListSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='cell-detail')

    class Meta:
        model = WarehouseCell
        fields = (
            'url',
            'rack',
            'tier',
            'position',
            'cell_width',
            'cell_height',
            'cell_length',
            'barcode',
        ) + AbstractSerializer.Meta.fields


class WarehouseSerializer(LoggerSerializer, AbstractSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='warehouse-detail')

    class Meta:
        model = Warehouse
        fields = (
            'url',
            'name',
            'owner',
            'created_at',
        ) + AbstractSerializer.Meta.fields
