from django.urls import path
from search import views


app_name = 'search'

urlpatterns = [
    path('result/', views.searchResult, name="s_results"),
    path('<str:category>/', views.category_func, name="category_func")
]

