# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from .models import Cart, CartItem
from products.models import Products

def add_to_cart(request):
    request.session.set_expiry(3000)
    
    try:
        active = request.session['cart']#code
    except:
        request.session['cart'] = 'Empty'
        
    if request.session['cart'] != 'Empty':
        cart = request.session['cart']
        
        #request.session['total_items'] = len(update_cart.products.all())
    else:
        new_cart = Cart()
        new_cart.save()
        request.session['cart'] = new_cart.id
        
    
    if request.method == 'POST':
        product_id = request.POST['product_id']
        quantity = request.POST['quantity']
        cart_obj = Cart.objects.get(id=request.session['cart'])
        cart_obj.active = True
        cart_obj.save()
        product_obj = Products.objects.get(id=product_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart_obj, product=product_obj)
        if created:
            print 'Created!'
        cart_item.quantity = quantity
        cart_item.save()
        print cart_item
        request.session['total_items'] = len(CartItem.objects.filter(cart=cart_obj))
    return HttpResponseRedirect('/products/')

def view(request):
    try:
        cart_id = request.session['cart']
        cart_exists = Cart.objects.get(id = cart_id)
    except:
        cart_exists = False
        try:
            request.session['total_items'] == 0 
        except:
            pass
    if cart_exists == False or cart_exists.active == False:
        message = "Your cart is empty!"
        
    if cart_exists and cart_exists.active:
        cart = CartItem.objects.filter(cart=cart_exists)
        
    return render_to_response('cart/cart.html', locals(), context_instance=RequestContext(request))

def delete(request):
    try:
        cart_id = request.session['cart']
        cart = Cart.objects.get(id=cart_id)
    except:
        cart = False
    if cart:
        deactivate = Cart.objects.get(id=cart_id)
        deactivate.active = False
        deactivate.save()
        request.session['total_items'] = 0
        
    return HttpResponseRedirect('/cart/')

    
