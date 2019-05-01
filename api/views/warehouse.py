from api.serializers import warehouse
from api.serializers.warehouse import CellSerializer, CellListSerializer, RackListSerializer
from base.viewsets import CreateListView
from warehouse.models import Warehouse, WarehouseCell, Rack


class WarehouseAPIView(CreateListView):
    queryset = Warehouse.objects.all()
    serializer_class = warehouse.WarehouseSerializer


class RackAPIView(CreateListView):
    queryset = Rack.objects.all()
    serializer_class = RackListSerializer


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

