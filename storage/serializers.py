from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from product.models import ContainerParams
from product.serializers import ProductSerializer
from warehouse.serializers import WarehouseCellSerializer
from .models import Storage, Container
from incoming.models import DocumentEntry


class ContainerTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContainerParams
        fields = (
            'name',

        )


class ContainerSerializer(serializers.ModelSerializer):
    cont_type = ContainerTypesSerializer(read_only=True)

    class Meta:
        model = Container
        fields = (
            'id',
            'cont_type',
            'barcode',
        )


class DocumentEntryViewSerializer(serializers.ModelSerializer):
    cell = WarehouseCellSerializer(read_only=True)
    container = ContainerSerializer(read_only=True)
    nomenclature = ProductSerializer(read_only=True)

    class Meta:
        model = DocumentEntry
        fields = (
            'id',
            'name',
            'cell',
            'nomenclature',
            'quantity',
            'container',


        )


class StorageViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Storage
        fields = (
            'id',
            'container'
        )


class StorageSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        DocumentEntry: DocumentEntryViewSerializer,
        Storage: StorageViewSerializer,
    }
