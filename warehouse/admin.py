from django.contrib import admin

from users.models import Warehouse
from .models import WarehouseCell, Rack

admin.site.register(WarehouseCell)
admin.site.register(Rack)
admin.site.register(Warehouse)
# Register your models here.
