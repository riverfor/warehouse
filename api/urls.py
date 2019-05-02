from django.conf.urls import url, include
from rest_framework import routers

from api.views.incoming import ExpectedAcceptanceListView
from api.views.product import ContainerClassViews, ProductModelView, ProductView, UnitClassView, UnitView
from api.views.warehouse import WarehouseAPIView, CellAPIView, RackAPIView
from base.viewsets import ProfileView

router = routers.DefaultRouter()
router.register(r'warehouses', WarehouseAPIView, base_name='warehouse')
router.register(r'racks', RackAPIView, base_name='rack')
router.register(r'cells', CellAPIView, base_name='cell')
router.register(r'container_classes', ContainerClassViews, base_name='container_class')
router.register(r'product_models', ProductModelView, base_name='product_model')
router.register(r'products', ProductView, base_name='product')
router.register(r'unit_classes', UnitClassView, base_name='unit_class')
router.register(r'units', UnitView, base_name='unit')

router.register(r'expected_acceptance', ExpectedAcceptanceListView, basename='expected_acceptance')

router.register(r'profile', ProfileView, base_name='profile')

urlpatterns = [
    url(r'^', include(router.urls)),
]
