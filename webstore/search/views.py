from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django import forms
from django.db.models import Q
from product.models import Product, Review
from django.core.paginator import Paginator


# Create your views here.

# def search(request):
#   content_list = Content.objects.all()
#   search = request.GET.get('search','')
#   if search:
#     search_list = content_list.filter(
#       Q(title__icontains = search) | #제목
#       Q(body__icontains = search) | #내용
#       Q(writer__username__icontains = search) #글쓴이
#     )
#   paginator = Paginator(search_list,5)
#   page = request.GET.get('page','')
#   posts = paginator.get_page(page)
#   board = Board.objects.all()
#
#   return render(request, 'search/post_search.html', {'posts':posts, 'Board':board, 'search':search})


def searchResult(request):
  if 'keyword' in request.GET:
    query = request.GET.get('keyword')
    products = Product.objects.all().filter(
      Q(p_name__icontains=query) |
      Q(p_summary_desc__icontains=query) |
      Q(p_category__icontains=query)
    )
    product_list = products
    page = request.GET.get('page', '1')
    paginator = Paginator(product_list, '8')
    page_obj = paginator.page(page)
    context = {
      'query': query,
      # 'page': page_obj,
      'products': products,
    }

  return render(request, 'search/search_result.html', context)


def category_func(request, category):
  products = Product.objects.all().filter(
    Q(p_category__icontains=category)
  )
  product_list = products
  page = request.GET.get('page', '1')
  paginator = Paginator(product_list, '8')
  page_obj = paginator.page(page)
  context = {
    'page': page_obj,
    'products': products,
  }

  return render(request, 'product/list.html', context)


def recommender(request):
  page = request.GET.get('page', '1')

  # 품절 임박 상품
  coming_sold = Product.objects.filter(p_stock__lt=5)
  sold_paginator = Paginator(coming_sold, '4')
  page_obj = sold_paginator.page(page)




  # 추천 상품
  rating = {}
  rating.clear()
  queryset1 = Product.objects.all()

  for i in queryset1:

    review_rate = Review.objects.filter(r_product__p_name=i.p_name)
    sum_rating = 0
    for j in review_rate:
      product_rating = {'★': 1, '★★': 2, '★★★': 3, '★★★★': 4, '★★★★★': 5}.get(j.r_point)
      sum_rating += product_rating

    rating[str(i.p_name)] = sum_rating

  high_rating = sorted(rating.items(), reverse=True, key=lambda item: item[1])

  index = list(high_rating)
  index_rate = []

  for i in range(0, 4):
    j = str(index[i][0])
    index_rate.append(j)

  recommed_product = Product.objects.filter(p_name__in=index_rate)

  context = {
    'index': high_rating,
    'page': page_obj,
    'recommend_product': recommed_product,
  }


  # return render(request, 'search/error.html', context)
  return render(request, 'search/index.html', context)


