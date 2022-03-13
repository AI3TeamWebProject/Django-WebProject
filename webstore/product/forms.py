from django import forms
from product.models import Product, Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['r_point', 'r_content', 'r_title']
        labels = {
            'r_point': '평점',
            'r_content': '내용',
            'r_title': '제목',
        }

