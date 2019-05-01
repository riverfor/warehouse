from users.models import User, Warehouse
from rest_framework import serializers


class WarehouseSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='warehouse-detail')

    class Meta:
        model = Warehouse
        fields = (
            'url',
            'name',
        )


class OwnerSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='profile-detail')

    class Meta:
        model = User
        fields = (
            'url',
            'first_name',
            'last_name',
            'warehouse',
            'email',
        )


class OwnerListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='profile-detail')
    warehouse = WarehouseSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'url',
            'first_name',
            'last_name',
            'warehouse',
            'email',
        )
