from django.conf.urls import url, include
from rest_framework import routers
from warehouse.viewsets import WarehouseAPIView
from storage.viewsets import StorageViewset

router = routers.DefaultRouter()
router.register(r'warehouse', WarehouseAPIView)
router.register(r'storage', StorageViewset)

urlpatterns = [
    url(r'^', include(router.urls)),

]