from django.contrib import admin

# Register your models here.
from incoming.models import DocumentPlan, DocumentProducts, DocumentEntry

admin.site.register(DocumentPlan)
admin.site.register(DocumentProducts)

admin.site.register(DocumentEntry)
