from rest_framework import serializers
from base.serializers import AbstractSerializer, LoggerSerializer
from users.models import Warehouse
from warehouse.models import Rack, WarehouseCell, Tier, Position, CELL_TYPE_CHOICES


class WarehouseSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='warehouse-detail')

    class Meta:
        model = Warehouse
        fields = (
            'url',
            'id',
            'name',
        )


class RackListSerializer(LoggerSerializer, AbstractSerializer):

    class Meta:
        model = Rack
        fields = (
            'id',
            'name',
        ) + AbstractSerializer.Meta.fields


class TierListSerializer(LoggerSerializer, AbstractSerializer):

    class Meta:
        model = Tier
        fields = (
            'id',
            'name',
        ) + AbstractSerializer.Meta.fields


class PositionListSerializer(LoggerSerializer, AbstractSerializer):

    class Meta:
        model = Position
        fields = (
            'id',
            'name',
        ) + AbstractSerializer.Meta.fields


class CellSerializer(LoggerSerializer):
    cell_type = serializers.ChoiceField(choices=CELL_TYPE_CHOICES)

    class Meta:
        model = WarehouseCell
        fields = (
            'id',
            'name',
            'cell_type',
            'rack',
            'tier',
            'position',
            'cell_width',
            'cell_height',
            'cell_length',

        )


class CellListSerializer(LoggerSerializer, AbstractSerializer):
    rack = RackListSerializer(read_only=True)
    tier = TierListSerializer(read_only=True)
    position = PositionListSerializer(read_only=True)
    cell_type = serializers.ChoiceField(choices=CELL_TYPE_CHOICES)

    class Meta:
        model = WarehouseCell
        fields = (
            'id',
            'name',
            'cell_type',
            'rack',
            'tier',
            'position',
            'cell_width',
            'cell_height',
            'cell_length',
            'barcode',
        ) + AbstractSerializer.Meta.fields
