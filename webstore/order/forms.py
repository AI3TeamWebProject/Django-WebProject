from django import forms
from order.models import OrderInfo
from order.models import Coupon


class OrderInfoForm(forms.ModelForm):
    class Meta:
        model = OrderInfo
        fields = '__all__'

        labels = {
            'o_name': '이름',
            'o_email': '이메일',
            'o_address': '주소',
            'o_detailAddress': '상세주소',
            'o_totalPrice': '총액',
            'o_mileage': '적립금',
        }

        widgets = {
            'o_name': forms.TextInput(
                attrs={
                    'class': 'form-control w-50'
                }
            ),
            'o_email': forms.EmailInput(
            ),
            'o_address': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'o_detailAddress': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            # 'o_totalPrice': forms.IntegerField(
            # ),
            # 'o_mileage': forms.IntegerField(
            # )
        }


# class cartInfoForm(forms.ModelForm):
#     class Meta:
