from product.models import Product, Review
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from product.forms import ReviewForm

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


def review_create(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.r_author = request.user
            review.r_product = product
            review.r_point = form.data['r_point']
            review.r_content = form.data['r_content']
            review.save()
            return redirect('product:p_detail', product_id=product_id)
    else:
        form = ReviewForm()

    context = {'form': form,
               'product_id': product_id,
               }
    return render(request, 'product/create_review.html', context)

