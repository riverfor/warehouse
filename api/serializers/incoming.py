from base.serializers import AbstractSerializer
from rest_framework import serializers
from incoming.models import DocumentPlan
from api.serializers.warehouse import CellSerializer


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

    class Meta:
        model = DocumentPlan
        fields = (
            'id',
            'cell',
            'bill',
            'bill_date',
            'comments',
        ) + AbstractSerializer.Meta.fields