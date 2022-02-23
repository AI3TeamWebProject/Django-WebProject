from django.shortcuts import render
from product.models import Item
from django.views.generic import DetailView

# Create your views here.

def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "home-page.html", context)


class ItemDetailView(DetailView):
    model = Item
    template_name = "product-page.html"

