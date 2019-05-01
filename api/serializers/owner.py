from rest_framework import serializers
from django.contrib.auth.models import User


class OwnerSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='profile-detail')

    class Meta:
        model = User
        fields = (
            'url',
            'first_name',
            'last_name',
            'email',
        )
