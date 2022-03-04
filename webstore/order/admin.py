from django.contrib import admin
from order.models import Coupon, OrderInfo, Cart, CartItem


# Register your models here.
admin.site.register(Coupon)
admin.site.register(OrderInfo)
admin.site.register(Cart)
admin.site.register(CartItem)
