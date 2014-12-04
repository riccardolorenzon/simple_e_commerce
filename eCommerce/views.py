from django.shortcuts import render, redirect
from models import Product

def cartItems(cart):
    items = []
    for item in items:
        items.append(Product.objects.get(id = item))
    return items

def priceCart(cart):
    cart_items = cartItems(cart)
    price = 0
    for item in cart_items:
        price += item.price
    return price

def catalog(request):
    if 'cart' not in request.session:
        request.session['cart'] = []
    cart = request.session['cart']
    request.session.set_expiry(0)
    store_items = Product.objects.all()

    ctx = {'store_items' : store_items, 'cart_items' : len(cart)}
    if request.method == 'POST':
        cart.append(int(request.POST['obj_id']))
        return redirect('catalog')
    return render(request, "catalog.html", ctx)

def cart(request):
    cart = request.session['cart']
    request.session.set_expiry(0)
    ctx = {'cart' : cart, 'cart_size' : len(cart), 'cart_items': cartItems(cart),
           'total_price' : priceCart(cart)}
    return render(request, "cart.html", ctx)
