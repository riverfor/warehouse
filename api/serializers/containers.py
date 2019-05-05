from base.serializers import AbstractSerializer, LoggerSerializer
from rest_framework import serializers

from product.models import ContainerParams
from storage.models import Container


class ContainerSerializer(LoggerSerializer, AbstractSerializer):

    class Meta:
        model = Container
        fields = (
            'id',
            'cont_type',
        ) + AbstractSerializer.Meta.fields


class ContainerListSerializer(LoggerSerializer, AbstractSerializer):

    class Meta:
        model = Container
        fields = (
            'id',
            'cont_type',
            'barcode',
        ) + AbstractSerializer.Meta.fields


class ContainerGenerateSerializer(serializers.Serializer):
    count = serializers.IntegerField(min_value=1, max_value=50)

    query = ContainerParams.objects.all()

    type = serializers.PrimaryKeyRelatedField(queryset=query)

    class Meta:
        fields = (
            'count',
            'type',
        )

