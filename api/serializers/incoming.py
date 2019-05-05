from base.serializers import AbstractSerializer
from rest_framework import serializers
from incoming.models import DocumentPlan, DocumentProducts, DocumentEntry
from api.serializers.warehouse import CellSerializer
from warehouse.models import WarehouseCell, ACCEPTANCE


class ExpectedAcceptanceListSerializer(serializers.ModelSerializer, AbstractSerializer):
    cell = CellSerializer(read_only=True)

    class Meta:
        model = DocumentPlan
        fields = (
            'id',
            'cell',
            'bill',
            'bill_date',
            'comments',
        ) + AbstractSerializer.Meta.fields


class ExpectedAcceptanceSerializer(serializers.ModelSerializer, AbstractSerializer):
    cell_query = WarehouseCell.objects.filter(cell_type=ACCEPTANCE)
    cell = serializers.PrimaryKeyRelatedField(queryset=cell_query)

    class Meta:
        model = DocumentPlan
        fields = (
            'id',
            'cell',
            'bill',
            'bill_date',
            'comments',
        ) + AbstractSerializer.Meta.fields


class AcceptanceProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentProducts
        fields = (
            'id',
            'document',
            'product',
            'unit',
            'plan',
        )


class AcceptanceProductsListSerializer(serializers.ModelSerializer):
    document = ExpectedAcceptanceSerializer(read_only=True)

    from api.serializers.product import ProductSerializer, UnitSerializer
    product = ProductSerializer(read_only=True)
    unit = UnitSerializer(read_only=True)

    class Meta:
        model = DocumentProducts
        fields = (
            'id',
            'document',
            'product',
            'unit',
            'plan',
            'fact',
        )


class AcceptanceEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentEntry
        fields = (
            'id',
            'name',
            'doc_plan',
            'nomenclature',
            'storage_unit',
            'quantity',
            'in_container',

        )
