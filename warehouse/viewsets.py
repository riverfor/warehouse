from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import WarehouseSerializer


class WarehouseAPIView(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

    def create(self, request, *args, **kwargs):
        return Response(data={'error': 'true'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def perform_create(self, serializer):
        if serializer.save(author=self.request.user):
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(data={'status': 'fail', 'message': 'not set'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'], name='Test actions')
    def custom(self, request, pk=None, cell_id=None):
        if self.request.query_params.get('radius', None):
            return Response({'status': 'ok', 'radius': self.request.query_params['radius']})
        else:
            return Response({'status': 'ok', 'radius': 'not set'})

