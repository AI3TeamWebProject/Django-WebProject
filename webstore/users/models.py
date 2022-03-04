from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Member(AbstractUser):
    mobile = models.CharField(max_length=20)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT,
                              blank=True,
                              null=True)
    postal_code = models.IntegerField(default=0, verbose_name='우편번호')
    address = models.CharField(max_length=50, verbose_name='주소'),
    address_detail = models.CharField(max_length=30, verbose_name='상세주소')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '고객'
        verbose_name_plural = '고객'
