from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from django.http import HttpResponse
from users.models import Member
from order.models import Cart, CartItem
from order.forms import OrderInfoForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


'''
장바구니 기능 구현
'''


def _cart_id(request):
  cart = request.session.session_key
  if not cart:
    cart = request.session.create()
  return cart


def add_cart(request, item_id):
  product = Product.objects.get(id=item_id)
  try:
      cart = Cart.objects.get(cart_id=_cart_id(request))
  except Cart.DoesNotExist:
      cart = Cart.objects.create(
        cart_id =_cart_id(request)
      )
      cart.save()

  try:
      cart_item = CartItem.objects.get(product=product, cart=cart)
      cart_item.quantity += 1
      cart_item.save()
  except CartItem.DoesNotExist:
      cart_item = CartItem.objects.create(
        product = product,
        quantity = 1,
        cart = cart
      )
      cart_item.save()
  return redirect('order:cart_detail')


def cart_detail(request, total=0, counter=0, cart_items = None):
  try:
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart, active=True)
    for cart_item in cart_items:
      total += (cart_item.product.p_supply_price * cart_item.quantity)
      counter += cart_item.quantity
  except ObjectDoesNotExist:
    pass

  return render(request, 'cart/cart_detail.html', dict(cart_items=cart_items, total=total, counter=counter))


def cart_remove(requset, item_id):
    cart = Cart.objects.get(cart_id=_cart_id(requset))
    product = get_object_or_404(Product, id=item_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity >1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('order:cart_detail')


def cart_plus(request, item_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=item_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('order:cart_detail')


def cart_delete(request, item_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=item_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('order:cart_detail')


def total_price(request):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.filter(cart=cart)
    total = 0
    for items in cart_item:
        total += (items.product.p_supply_price * items.quantity)

    return total


def checkout(request):

    if request.method == 'POST':
        order_form = OrderInfoForm(request.POST)
        user_id = _cart_id(request)

        cart_item = CartItem.objects.filter(cart=user_id, active=True)

        if order_form.is_valid():
            order_form.save()
            context = {
                'order_form': order_form,
                'order_item': cart_item,

            }
            return render(request, 'order/payments.html', context)

        else:
            return HttpResponse('error!')

    elif request.method == 'GET':
        seesion_key = _cart_id(request)
        order_form = OrderInfoForm()
        cart_item = CartItem.objects.filter(cart=seesion_key)
        total = total_price(request)
        context = {
            'order_form': order_form,
            'order_item': cart_item,
            'total': total,
        }

        return render(request, 'order/checkout.html', context)

    else:
        order_form = OrderInfoForm()
        context = {
            'order_form': order_form
        }
        return render(request, 'order/checkout.html', context)

