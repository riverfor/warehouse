from rest_framework import viewsets, mixins
from api.serializers.warehouse import CellSerializer, CellListSerializer, RackListSerializer, WarehouseSerializer, \
    TierListSerializer, PositionListSerializer
from base.viewsets import CreateListView
from users.models import Warehouse
from warehouse.models import WarehouseCell, Rack, Tier, Position


class WarehouseAPIView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class RackAPIView(CreateListView):
    queryset = Rack.objects.all()
    serializer_class = RackListSerializer


class TierAPIView(CreateListView):
    queryset = Tier.objects.all()
    serializer_class = TierListSerializer


class PositionAPIView(CreateListView):
    queryset = Position.objects.all()
    serializer_class = PositionListSerializer


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
    queryset = WarehouseCell.objects.all().order_by('-rack').order_by('-tier').order_by('-position')

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, CellSerializer)

