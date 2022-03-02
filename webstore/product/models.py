from django.db import models
from django.conf import settings


CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    # shipping_address = models.ForeignKey(
    #     'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    # billing_address = models.ForeignKey(
    #     'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    # payment = models.ForeignKey(
    #     'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    # coupon = models.ForeignKey(
    #     'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    # being_delivered = models.BooleanField(default=False)
    # received = models.BooleanField(default=False)
    # refund_requested = models.BooleanField(default=False)
    # refund_granted = models.BooleanField(default=False)

    '''
    1. Item added to cart
    2. Adding a billing address
    (Failed checkout)
    3. Payment
    (Preprocessing, processing, packaging etc.)
    4. Being delivered
    5. Received
    6. Refunds
    '''

    def __str__(self):
        return self.user

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        # if self.coupon:
        #     total -= self.coupon.amount
        return total


class Category(models.Model):
    # 카테고리 id에 맞춰서 중분류 명을 배분.
    c_category = models.CharField(max_length=20)

    def __str__(self):
        return self.c_category


class ProductColor(models.Model):
    # id에 맞춰서 컬러를 배분.
    c_color = models.CharField(max_length=20)

    def __str__(self):
        return self.c_color


class ProductSize(models.Model):
    # id에 맞춰서 사이즈를 배분
    s_size = models.CharField(max_length=20)

    def __str__(self):
        return self.s_size


class Product(models.Model):
    p_name = models.CharField(max_length=15)  #이름
    p_category = models.ForeignKey(Category, on_delete=models.CASCADE)  #카테고리
    p_soldOut = models.BooleanField(default=True)    # 품절
    p_summary_desc = models.CharField(max_length=70)   #요약 정보
    p_simple_desc = models.CharField(max_length=140)    # 간단정보
    p_detail_desc = models.CharField(max_length=300)    #상세정보
    p_supply_price = models.IntegerField(default=0)   #공급가
    p_real_price = models.IntegerField(default=0)     #실제 판매가
    p_discount = models.IntegerField(default=0)       # 할인율
    p_color = models.ForeignKey(ProductColor, on_delete=models.CASCADE)      # 색상
    p_size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)       # 사이즈
    p_register_date = models.DateTimeField(auto_now=True)      #등록일

    def __str__(self):
        return self.p_name

