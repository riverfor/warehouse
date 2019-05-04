from base.viewsets import CreateListView
from api.serializers.incoming import ExpectedAcceptanceListSerializer, DocumentPlan, ExpectedAcceptanceSerializer, \
    AcceptanceProductsSerializer, DocumentProducts, AcceptanceProductsListSerializer


class ExpectedAcceptanceListView(CreateListView):
    queryset = DocumentPlan.objects.all()

    def get_serializer_class(self):
        if self.action == 'update' or self.action == "create":
            return ExpectedAcceptanceSerializer
        else:
            return ExpectedAcceptanceListSerializer


class AcceptanceProductsView(CreateListView):
    queryset = DocumentProducts.objects.all()

    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'create':
            return AcceptanceProductsSerializer
        else:
            return AcceptanceProductsListSerializer
