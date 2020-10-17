from django.urls import path
from . import views


name = 'store'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('item/', views.ItemList.as_view(), name='items'),
    path('item/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('store/', views.StoreList.as_view(), name='stores'),
    path('store/<int:pk>/', views.StoreDetail.as_view(), name='store-detail'),
    path('inventory/', views.InventoryList.as_view(), name='inventory'),
    path('inventory/<int:pk>/', views.InventoryDetail.as_view(), name='inventory-detail'),
    path('inv_has_item/', views.InventoryHasItemList.as_view(), name='inv-has-item'),
    path('inv_has_item/<int:pk>/', views.InventoryHasItemDetail.as_view(), name='inv-has-item-detail')
]