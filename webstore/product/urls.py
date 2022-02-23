from django.urls import path
from product import views


app_name = 'product'

# http://127.0.0.1:8000/

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('product/<slug>/<int:item_id>', views.ItemDetailView, name='ItemDetailView'),
]
