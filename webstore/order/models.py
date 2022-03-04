from django.db import models
from product.models import Item
from users.models import Member

# Create your models here.

class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class OrderInfo(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="ordered_user")
    o_code = models.CharField(max_length=15)
    o_name = models.CharField(max_length=20)
    o_email = models.CharField(max_length=50)
    o_address = models.CharField(max_length=100)
    o_detailAddress = models.CharField(max_length=100)
    o_totalPrice = models.FloatField()
    o_mileage = models.IntegerField()
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.o_name

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True, primary_key=True)
    cart_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['cart_date']

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "CartItem"

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.title

