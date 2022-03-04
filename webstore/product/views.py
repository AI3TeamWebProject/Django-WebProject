from product.models import Product
from django.shortcuts import render, redirect, get_object_or_404

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
    context = {
        'product': product
    }
    return render(request, 'product/detail.html', context)



