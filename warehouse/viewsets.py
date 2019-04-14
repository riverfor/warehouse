from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import WarehouseSerializer, Warehouse
from rest_framework.schemas import AutoSchema
from rest_framework.compat import coreapi, coreschema


class WarehouseShema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if path.endswith('/custom/'):
            extra_fields = [
                coreapi.Field(
                    "cell_id",
                    required=True,
                    location="form",
                    schema=coreschema.Integer()
                ),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class WarehouseViewset(viewsets.ModelViewSet):
    serializer_class = WarehouseSerializer
    queryset = Warehouse.objects.all()

    schema = WarehouseShema()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['post'], name='Test actions')
    def custom(self, request, pk=None, cell_id=None):
        if self.request.query_params.get('radius', None):
            return Response({'status': 'ok', 'radius': self.request.query_params['radius']})
        else:
            return Response({'status': 'ok', 'radius': 'not set'})

