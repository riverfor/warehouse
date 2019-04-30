from api.serializers.product import ContainerClassSerializer, ContainerParams, ProductModelSerializer, \
    AccountingModelProducts, Product, ProductListSerializer, ProductSerializer, UnitClassSerializer, StorageUnitsClass, \
    StorageUnit, UnitSerializer, UnitListSerializer, UnitEditSerializer
from base.viewsets import CreateListView


class ContainerClassViews(CreateListView):
    serializer_class = ContainerClassSerializer
    queryset = ContainerParams.objects.all()


class ProductModelView(CreateListView):
    serializer_class = ProductModelSerializer
    queryset = AccountingModelProducts.objects.all()


class ProductView(CreateListView):
    queryset = Product.objects.all()
    serializer_clases = {
        'list': ProductListSerializer,
        'get': ProductListSerializer,
        'retrieve': ProductListSerializer,
        'create': ProductSerializer,
        'update': ProductSerializer,

    }

    def get_serializer_class(self):
        return self.serializer_clases.get(self.action, ProductSerializer)


class UnitClassView(CreateListView):
    serializer_class = UnitClassSerializer
    queryset = StorageUnitsClass.objects.all()


class UnitView(CreateListView):
    queryset = StorageUnit.objects.all()
    serializer_clases = {
        'list': UnitListSerializer,
        'get': UnitListSerializer,
        'retrieve': UnitListSerializer,
        'create': UnitSerializer,
        'update': UnitEditSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_clases.get(self.action, UnitSerializer)
