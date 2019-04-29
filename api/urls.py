from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers

from product.viewsets import ProductViewset, AccountingModelViewset, StorageUnitsClassViewset, StorageUnitViewset
from warehouse.viewsets import WarehouseAPIView
from storage.viewsets import StorageViewset, DocumentIncomingViewset, DocumentPlanViewSet, DocumentProductsViewset

router = routers.DefaultRouter()
router.register(r'warehouse', WarehouseAPIView)
router.register(r'storage', StorageViewset)
router.register(r'incoming_entry', DocumentIncomingViewset)
router.register(r'documents_plan', DocumentPlanViewSet)
router.register(r'document_products', DocumentProductsViewset, base_name='document_products')
router.register(r'products', ProductViewset, base_name='product')
router.register(r'accounting_models', AccountingModelViewset, base_name='accounting_model')
router.register(r'units_classes', StorageUnitsClassViewset, base_name='unit_class')
router.register(r'units', StorageUnitViewset, base_name='unit')

urlpatterns = [
    url(r'^', include(router.urls)),
]
