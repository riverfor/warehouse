from rest_framework import serializers
from warehouse.models import Warehouse, Rack, WarehouseCell


class RackListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rack
        fields = (
            'id',
            'name',
        )


class CellSerializer(serializers.ModelSerializer):
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


class CellListSerializer(serializers.ModelSerializer):
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
        )


class WarehouseSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='warehouse-detail')

    class Meta:
        model = Warehouse
        fields = (
            'url',
            'name',
        )
