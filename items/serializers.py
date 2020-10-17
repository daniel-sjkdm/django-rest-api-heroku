from rest_framework import serializers
from django.contrib.gis.geos import Point
from .models import Store, Inventory, InventoryHasItem, Item



class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = [
            'name',
            'address',
            'location'
        ]


    def create(self, validated_data):
        name = self.validated_data['name']
        address = self.validated_data['address']
        x, y = self.validated_data['location'].split(",")
        location = Point(float(x), float(y))

        return Store.objects.create(
            name=name,
            address=address,
            location=location
        )



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