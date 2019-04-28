from django.conf.urls import url, include
from rest_framework import routers
from warehouse.viewsets import WarehouseAPIView

router = routers.DefaultRouter()
router.register(r'warehouse', WarehouseAPIView)

urlpatterns = [
    url(r'^', include(router.urls)),

]