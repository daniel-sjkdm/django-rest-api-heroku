from django.contrib import admin
from .models import Store, Inventory, InventoryHasItem, Item


admin.site.register(Store)
admin.site.register(Inventory)
admin.site.register(InventoryHasItem)
admin.site.register(Item)