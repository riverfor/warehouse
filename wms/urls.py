from django.conf.urls import url, include
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from django.contrib import admin

shema_view = get_swagger_view(title='Warehouse managment system API')

urlpatterns = [
    path('api/v1/', include("api.urls")),
    url(r'^admin', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^swagger$', shema_view),
]