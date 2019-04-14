from rest_framework import serializers
from .models import Warehouse
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
