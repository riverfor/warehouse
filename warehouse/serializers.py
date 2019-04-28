from rest_framework import serializers
from .models import Warehouse, WarehouseCell, Rack
from django.contrib.auth.models import User


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields = (
            'id',
            'email',
        )


class WarehouseSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Warehouse
        fields = (
            'id',
            'name',
            'blocked',
            'author',
        )


class RackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rack
        fields = (
            'id',
            'name',
        )


class WarehouseCellSerializer(serializers.ModelSerializer):
    rack = RackSerializer(read_only=True)

    class Meta:
        model = WarehouseCell
        fields = (
            'rack',
            'tier',
            'position',
        )