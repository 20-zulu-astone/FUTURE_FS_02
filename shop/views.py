from django.shortcuts import render,get_object_or_404, redirect
from .models import cartitem, products,Order
from django.db.models import Q
from .forms import OrderForm
from django.utils import timezone

"""def carts(request):
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = products.objects.get(id=product_id)
        subtotal = product.price * quantity
        total = 0
        total += int(subtotal)
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })"""
def carts(request):
    cart = request.session.get('cart', {})  # { '1': 2, '3': 1 }
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(products, id=product_id)
        subtotal = int(product.price * quantity)
        total += subtotal  # add instead of resetting
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
        request.session.modified = True

    return redirect('carts')

def home(request):

    query = request.GET.get('q') 
     # None if not searching
    if query:
        all_product = products.objects.filter(name__icontains=query)
    else:
        all_product = products.objects.all()

    return render(request, 'home.html', {
        'all_product': all_product,
        'query': query
    })
   

  

"""def checkout(request):
    cart = request.session.get('cart', {})
    # Build order and order items from cart here
    # For example, create an Order instance and related OrderItems
    # For demo, let’s just show cart data for now
    order_summary = []  # build this from cart and products like in carts view
    total = 0
    for product_id, qty in cart.items():
        product = products.objects.get(id=product_id)
        subtotal = int(product.price * qty)
        total += subtotal
        order_summary.append({
            'product': product,
            'quantity': qty,
            'subtotal': subtotal
        })

    return render(request, 'order.html', {
        'order_summary': order_summary,
        'total': total
    })"""

"""def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        # If cart empty, redirect back or show message
        return redirect('cart')
    order = None


    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()  # No user attached
            # TODO: Save order items from cart here (optional)

            # Clear cart from session after order is placed
            request.session['cart'] = {}
            return redirect('success_order')
    else:
        form = OrderForm()

    return render(request, 'checkout.html', {'form': form})"""
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            # TODO: Save order items from cart here if needed

            # Mark payment status as paid directly (since payment is included)
            order.payment_status = 'paid'
            order.paid_at = timezone.now()
            order.save()

            # Clear cart after order + payment
            request.session['cart'] = {}

            return redirect('success_order')
    else:
        form = OrderForm()

    return render(request, 'checkout.html', {'form': form})


def success_order(request):
    return render(request,'success.html')

def add_to_cart(request, product_id):
    print("Form submitted")
    print("Product ID", product_id)
    product = get_object_or_404(products, id=product_id)

    # Get the cart from the session (or create a new one)
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1  # Increase quantity
    else:
        cart[str(product_id)] = 1  # Add for the first time

    # Save back to session
    request.session['cart'] = cart
    request.session.modified = True


    return redirect('home')  # Or wherever you want


def mock_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        order.payment_method = payment_method
        order.payment_status = 'paid'
        order.paid_at = timezone.now()
        order.save()
        return redirect('success_order')  # or wherever you want

    # If GET, just redirect or show a message
    return redirect('checkout')


    
