from django.db import models
from users.models import Member

CATEGORY_CHOICES = (
    ('T', 'T-Shirt'),
    ('OW', 'Outwear'),
    ('J', 'Jacket'),
    ('dr', 'Dress'),
    ('knit', 'knit'),
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

REVIEW_POINT_CHOICES = (
    ('★', '★'),
    ('★★', '★★'),
    ('★★★', '★★★'),
    ('★★★★', '★★★★'),
    ('★★★★★', '★★★★★'),
)

class Product(models.Model):
    p_name = models.CharField(max_length=30)
    p_category = models.CharField(choices=CATEGORY_CHOICES, max_length=5)
    p_soldOut = models.BooleanField(default=False)
    p_summary_desc = models.CharField(max_length=70)
    p_simple_desc = models.CharField(max_length=140)
    p_detail_desc = models.CharField(max_length=500)
    p_supply_price = models.IntegerField(default=0)
    p_price = models.IntegerField(default=0)
    p_discount = models.IntegerField(default=0)
    p_register_date = models.DateTimeField(auto_now=True)
    p_image_thumb = models.ImageField(upload_to='static/img/')
    p_stock = models.IntegerField(verbose_name='재고')
    # p_color = models.ForeignKey(ProductColor, on_delete=models.CASCADE)
    # p_size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)

    def __str__(self):
        return self.p_name

    class Meta:
        verbose_name = '상품'
        verbose_name_plural = '상품'
        ordering = ['-p_register_date', ]


class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img/')


class Review(models.Model):
    r_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    r_point = models.CharField(choices=REVIEW_POINT_CHOICES, max_length=10)
    r_title = models.CharField(max_length=50)  # 글 제목
    r_author = models.ForeignKey(Member, on_delete=models.CASCADE)
    r_content = models.CharField(max_length=200)  # 글 내용
    r_date = models.DateTimeField(auto_now=True)  # 글 작성시간
    r_image = models.ImageField(upload_to='static/img/', null=True)

    def __str__(self):
        return self.r_title

    class Meta:
        verbose_name = '리뷰'
        verbose_name_plural = '리뷰'
        ordering = ['-r_date', ]

