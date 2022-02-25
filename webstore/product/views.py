from product.models import Product
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

# Create your views here.


def p_detail(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, "detail.html", context)