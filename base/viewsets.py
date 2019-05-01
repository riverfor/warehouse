from django.contrib.auth.models import User
from rest_framework import mixins, viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.serializers.owner import OwnerSerializer


class ProfileView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):

    serializer_class = OwnerSerializer
    queryset = User.objects.all()

    def list(self, request):
        serializer_context = {
            'request': request,
        }
        queryset = self.queryset
        obj = get_object_or_404(queryset, pk=request.user.pk)
        serializer = self.serializer_class(obj, context=serializer_context)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        serializer_context = {
            'request': request,
        }
        queryset = self.queryset
        obj = get_object_or_404(queryset, pk=request.user.pk)
        serializer = self.serializer_class(obj, context=serializer_context)
        return Response(serializer.data)

    def update(self, request, pk=None):
        serializer_context = {
            'request': request,
        }
        queryset = self.queryset
        obj = get_object_or_404(queryset, pk=request.user.pk)
        serializer = self.serializer_class(obj, context=serializer_context)
        return Response(serializer.data)


class CreateListView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, viewsets.GenericViewSet):

    def perform_create(self, serializer):
        if serializer.save(owner=self.request.user):
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'fail', 'message': 'not set'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

