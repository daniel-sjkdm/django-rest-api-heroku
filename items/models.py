from django.db import models
from .validators import price_validator


class Store(models.Model):
    name = models.CharField(
            max_length=100, 
            null=False
    )
    address = models.CharField(
            max_length=150, 
            null=False
    )
    location = models.JSONField(null=True)

    class Meta:
        ordering = ['name']
        db_table = 'store'


    def __str__(self):
        return self.name



class Item(models.Model):
    name = models.CharField(
            max_length=100, 
            null=False
    )
    description = models.CharField(
            max_length=250, 
            null=False
    )
    price = models.DecimalField(
            max_digits=10, 
            decimal_places=2, 
            null=False,
            validators=[price_validator])
    img = models.ImageField(
            null=True
    )

    class Meta:
        ordering = ['name']
        db_table = 'item'

    def __str__(self):
        return self.name



class Inventory(models.Model):
    name = models.CharField(
            max_length=2, 
            null=False,
            unique=True
    )
    store = models.ForeignKey(
            Store, 
            null=False, 
            on_delete=models.CASCADE
    )
    has_item = models.ManyToManyField(
        Item,
        through='InventoryHasItem'
    )
    
    class Meta:
        ordering = ['store']
        db_table = 'inventory'

    def __str__(self):
        return self.name



class InventoryHasItem(models.Model):
    inventory_id = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    items = models.PositiveSmallIntegerField(null=False, default=0)
    
    class Meta:
        ordering = ['items']
        db_table = 'inv_has_item'

    def __str__(self):
        return f"Inventory {self.inventory_id} has [{self.items}] {self.item_id}"