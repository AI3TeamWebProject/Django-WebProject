from django.db import models
from users.models import Member
# Create your models here.


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

