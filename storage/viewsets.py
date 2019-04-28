from rest_framework import viewsets
from .serializers import StorageSerializer, DocumentEntryViewSerializer
from .models import Storage


class StorageViewset(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer