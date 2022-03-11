from product.models import Product, Review
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

# def index(request):
#     if request.user.is_authenticated:
#         products = Product.objects.all().order_by('-p_register_date')
#         context = {
#             'products': products
#         }
#         return render(request, 'home.html', context)
#     else:
#         return redirect('home')


def index(request):
    products = Product.objects.all().order_by('-p_register_date')
    context = {
        'products': products
    }
    return render(request, 'home.html', context)


def p_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    reviews = Review.objects.filter(r_product=product)
    context = {
        'product': product,
        'reviews': reviews
    }
    return render(request, 'product/detail.html', context)



## list page

def p_list(request):
    product = Product.objects.all().order_by('-p_register_date')
    product_list = Product.objects.all()
    page = request.GET.get('page', '1')
    paginator = Paginator(product_list, '8')
    page_obj = paginator.page(page)
    context = {
        'prodcut': product,
        'page': page_obj,
    }
    return render(request, 'product/list.html', context)


