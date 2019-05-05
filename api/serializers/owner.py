from users.models import User
from rest_framework import serializers


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'warehouse',
        )
