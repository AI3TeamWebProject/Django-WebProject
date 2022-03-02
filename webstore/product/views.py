from product.models import Product
from django.shortcuts import render, redirect, get_object_or_404


def p_detail(request, product_id):
    # item = get_object_or_404(Product, pk=product_id)
    context = {
        'products': Product.objects.all()
    }
    return render(request, "product/detail.html", context)