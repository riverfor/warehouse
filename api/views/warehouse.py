from rest_framework import status
from rest_framework.response import Response

from api.serializers import warehouse
from api.serializers.warehouse import CellSerializer, CellListSerializer
from base.viewsets import CreateListView
from warehouse.models import Warehouse, WarehouseCell


class WarehouseAPIView(CreateListView):
    queryset = Warehouse.objects.all()
    serializer_class = warehouse.WarehouseSerializer

    def perform_create(self, serializer):
        if serializer.save(author=self.request.user):
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'fail', 'message': 'not set'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CellAPIView(CreateListView):
    """
    Список складских ячеек
    """
    serializer_classes = {
        'list': CellListSerializer,
        'get': CellListSerializer,
        'retrieve': CellListSerializer,
        'create': CellSerializer,
        'update': CellSerializer,

    }
    queryset = WarehouseCell.objects.all()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, CellSerializer)

