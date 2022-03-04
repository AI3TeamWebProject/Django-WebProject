from django.urls import path
from order import views


app_name = 'order'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('', views.cart_detail, name='cart_detail'),
    path('add/<item_id>/', views.add_cart, name="add_cart"),
    path('remove/<int:item_id>/', views.cart_remove, name="remove_cart"),
    path('plus/<int:item_id>', views.cart_plus, name="plus_cart"),
    path('delete/<int:item_id>/', views.cart_delete, name="delete_cart"),
    path('total/', views.total_price, name="total_price"),
]

