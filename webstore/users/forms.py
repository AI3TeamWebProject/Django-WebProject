from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from users.models import Member

class UserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Member
        fields = ("username", "password1", "password2", "email", "address")

class LoginForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['username', 'password']

        labels = {
            'username': '사용자이름',
            'password': '비밀번호'
        }

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '사용자이름을 입력하세요'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '비밀번호를 입력하세요'
                }
            )
        }
