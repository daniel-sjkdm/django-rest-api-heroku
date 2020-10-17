from .models import Store, Inventory, InventoryHasItem, Item
from .serializers import StoreSerializer, InventorySerializer, InventoryHasItemSerializer, ItemSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status




class IndexView(APIView):
	def get(self, request):
		data = {	
			'store': {
				'list': { 
					'url': '127.0.0.1:8000/api/store',
				},
				'detail': {
					'url': '127.0.0.1:8000/api/store/<int:pk>'
				}
			},
			'inventory': {
				'list': { 
					'url': '127.0.0.1:8000/api/inventory',
				},
				'detail': {
					'url': '127.0.0.1:8000/api/inventory/<int:pk>'
				}
			},
			'inventory-has-items': {
				'list': { 
					'url': '127.0.0.1:8000/api/inv_has_item',
				},
				'detail': {
					'url': '127.0.0.1:8000/api//<int:pk>'
				}
			},
			'item': {
				'list': { 
					'url': '127.0.0.1:8000/api/item',
				},
				'detail': {
					'url': '127.0.0.1:8000/api/item/<int:pk>'
				}
			},		
		}
		return Response(data, status=status.HTTP_200_OK)


class ItemList(generics.ListCreateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

	def get_queryset(self):
		items = Item.objects.all()
		return items


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer


class StoreList(generics.ListCreateAPIView):
	queryset = Store.objects.all()
	serializer_class = StoreSerializer



class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Store.objects.all()
	serializer_class = StoreSerializer


class InventoryList(generics.ListCreateAPIView):
	queryset = Inventory.objects.all()
	serializer_class = InventorySerializer



class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Inventory.objects.all()
	serializer_class = InventorySerializer



class InventoryHasItemList(generics.ListCreateAPIView):
	queryset = InventoryHasItem.objects.all()
	serializer_class = InventoryHasItemSerializer



class InventoryHasItemDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = InventoryHasItem
	serializer_class = InventoryHasItemSerializer