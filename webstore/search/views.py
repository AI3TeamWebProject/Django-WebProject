from django.shortcuts import render
from django import forms
from django.db.models import Q
from product.models import Product

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
      Q(p_category__c_category__icontains=query)
    )

  return render(request, 'search/search_result.html', {"query": query, "products": products})


def searchBox(request):

  return render(request, 'search/post_search.html')

