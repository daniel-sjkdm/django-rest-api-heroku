from rest_framework import serializers
from .models import Store, Inventory, InventoryHasItem, Item



class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = [
            'name',
            'address',
            'location'
        ]


class InventorySerializer(serializers.ModelSerializer):
    store = serializers.SlugRelatedField(
        slug_field="name", 
        read_only=False, 
        queryset=Store.objects.all()
    )
    has_item = serializers.SlugRelatedField(
        slug_field="name", 
        many=True, 
        read_only=True,
    )
    class Meta:
        model = Inventory
        fields = [
            'name',
            'store',
            'has_item'
        ]



class InventoryHasItemSerializer(serializers.ModelSerializer):
    inventory_id = serializers.SlugRelatedField(
        slug_field='name',
        read_only=False,
        queryset=Inventory.objects.all()
    )
    item_id = serializers.SlugRelatedField(
        slug_field='name',
        read_only=False,
        queryset=Item.objects.all()
    )
    class Meta:
        model = InventoryHasItem
        fields = [
            'inventory_id',
            'item_id',
            'items'
        ]


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'name',
            'description',
            'price',
            'img'
        ]