from rest_framework import status
from rest_framework.response import Response
from django.db import transaction

from api.serializers.containers import ContainerSerializer, ContainerListSerializer, ContainerGenerateSerializer
from base.viewsets import CreateListView
from product.models import ContainerParams
from storage.models import Container
from rest_framework.decorators import action


class ContainerAPIView(CreateListView):
    queryset = Container.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return ContainerSerializer
        elif self.action == 'generate':
            return ContainerGenerateSerializer
        else:
            return ContainerListSerializer

    @action(detail=False, methods=['post'])
    @transaction.atomic
    def generate(self, request):
        containers = []
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            count = serializer.data.get('count')
            cont_type = ContainerParams.objects.get(pk=serializer.data.get('type'))
            i = 1
            while i <= count:
                obj = Container.objects.create(cont_type=cont_type, owner=request.user)
                containers.append(ContainerListSerializer(obj).data)
                i += 1
            return Response(containers, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
