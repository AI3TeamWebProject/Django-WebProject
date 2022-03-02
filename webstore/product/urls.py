
from django.urls import path
from product import views


# http://127.0.0.1:8000/product/

app_name = 'product'

urlpatterns = [
    path('<int:product_id>/detail/', views.p_detail, name="p_detail"),
]
