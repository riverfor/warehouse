from django.conf.urls import url, include
from rest_framework import routers
from warehouse.viewsets import WarehouseViewset

router = routers.DefaultRouter()
router.register(r'warehouse', WarehouseViewset)

urlpatterns = [
    url(r'^', include(router.urls)),

]