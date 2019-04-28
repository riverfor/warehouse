from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from warehouse.serializers import WarehouseCellSerializer
from .models import Storage
from incoming.models import DocumentEntry


class DocumentEntryViewSerializer(serializers.ModelSerializer):
    cell = WarehouseCellSerializer(read_only=True)

    class Meta:
        model = DocumentEntry
        fields = (
            'id',
            'name',
            'cell',
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
