from django.urls import path
from search import views


app_name = 'search'

urlpatterns = [
    path('box/', views.searchBox, name='s_box'),
    path('result/', views.searchResult, name="s_results")
]

