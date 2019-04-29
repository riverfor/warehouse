from rest_framework import viewsets

from incoming.models import DocumentEntry, DocumentPlan, DocumentProducts
from .serializers import StorageSerializer, DocumentEntryViewSerializer, DocumentPlanSerializer, \
    DocumentPlanProductSerializer
from .models import Storage


class StorageViewset(viewsets.ModelViewSet):

    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


class DocumentPlanViewSet(viewsets.ModelViewSet):
    queryset = DocumentPlan.objects.all()
    serializer_class = DocumentPlanSerializer


class DocumentProductsViewset(viewsets.ModelViewSet):
    queryset = DocumentProducts.objects.all()
    serializer_class = DocumentPlanProductSerializer


class DocumentIncomingViewset(viewsets.ModelViewSet):
    queryset = DocumentEntry.objects.all()
    serializer_class = DocumentEntryViewSerializer
