from rest_framework import serializers

from api.serializers.owner import OwnerSerializer


class AbstractSerializer(serializers.Serializer):
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S", label='Создано в', read_only=True)
    updated_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S", label='Создано в', read_only=True)

    owner = OwnerSerializer(read_only=True, many=False)

    class Meta:
        fields = (
            'created_at',
            'updated_at',
            'owner',
        )
        abstract = True
