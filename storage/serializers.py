from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from product.models import ContainerParams
from product.serializers import ProductSerializer
from .models import Storage, Container
from incoming.models import DocumentEntry, DocumentPlan, DocumentProducts


class ContainerTypesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContainerParams
        fields = (
            'name',

        )


class ContainerSerializer(serializers.HyperlinkedModelSerializer):
    cont_type = ContainerTypesSerializer(read_only=True)

    class Meta:
        model = Container
        fields = (
            'id',
            'cont_type',
            'barcode',
        )


class DocumentPlanProductSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = DocumentProducts
        fields = (
            'url',
            'product',
        )


class DocumentPlanSerializer(serializers.ModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='document_product-detail')

    class Meta:
        model = DocumentPlan
        fields = (
            'cell',
            'products',
        )


class DocumentEntryViewSerializer(serializers.HyperlinkedModelSerializer):
    doc_plan = DocumentPlanSerializer(required=True, many=False)

    class Meta:
        model = DocumentEntry
        fields = (
            'url',
            'name',
            'doc_plan',

        )


class StorageViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Storage
        fields = (
            'id',
            'container',
            'doc_plan',
        )


class StorageSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        DocumentEntry: DocumentEntryViewSerializer,
        Storage: StorageViewSerializer,
    }
