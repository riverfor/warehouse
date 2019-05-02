from rest_framework import serializers
from base.serializers import AbstractSerializer, LoggerSerializer
from warehouse.models import Rack, WarehouseCell


class RackListSerializer(LoggerSerializer, AbstractSerializer):

    class Meta:
        model = Rack
        fields = (
            'id',
            'name',
        ) + AbstractSerializer.Meta.fields


class CellSerializer(LoggerSerializer):

    class Meta:
        model = WarehouseCell
        fields = (
            'id',
            'rack',
            'tier',
            'position',
            'cell_width',
            'cell_height',
            'cell_length',

        )


class CellListSerializer(LoggerSerializer, AbstractSerializer):
    rack = RackListSerializer(read_only=True)

    class Meta:
        model = WarehouseCell
        fields = (
            'id',
            'rack',
            'tier',
            'position',
            'cell_width',
            'cell_height',
            'cell_length',
            'barcode',
        ) + AbstractSerializer.Meta.fields
