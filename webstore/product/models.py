from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField


# 아래 CHOICES들의 쓰임새&의미는 아직 파악하지 않은 상태입니다.
# 일단 에러방지용으로 넣어두겠습니다.

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

####

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    # discount_price = models.FloatField(blank=True, null=True)
    # category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    # label = models.CharField(choices=LABEL_CHOICES, max_length=20)
    # slug = models.SlugField()
    # description = models.TextField()
    # image = models.ImageField()

    def __str__(self):
        return self.title

# slug
# Red Ribbon Dress 라는 대소문자와 띄어쓰기가 혼합된 제품명을
# red-ribbon-dress 로 변환하여 url에 표시하기 위해 사용하는 기능으로 파악됩니다.
# 가령 메인화면에서 제품 클릭시의 request url이 detail/<slug>/<int:item_id>/ 이라면,
# http://~~/detail/red-ribbon-dress/27/ 로 표시됩니다.
# 필수 기능은 아니지만 종종 사용되는 개념같아 적용시켜 보겠습니다.




# Item -> OrderItem -> Order 의 순서를 만듦으로써
# 장바구니를 컨트롤 할 수 있는 것으로 파악됩니다.

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# 장바구니에 들어갈 주문정보
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add = True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username



