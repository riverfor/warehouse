from users.models import User, Warehouse
from rest_framework import serializers


class WarehouseSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='warehouse-detail')

    class Meta:
        model = Warehouse
        fields = (
            'url',
            'id',
            'name',
        )


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'warehouse',
            'email',
        )


class OwnerListSerializer(serializers.ModelSerializer):
    warehouse = WarehouseSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'warehouse',
            'email',
        )
