# Jos rekisteröi tällä tavalla adminille oman appin
# modelit, voi myös admin sivulta muokata näitä tietoja.

from django.contrib import admin

from app.models import Supplier, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass

# Register your models here.
