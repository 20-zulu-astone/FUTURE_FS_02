from django.shortcuts import render,get_object_or_404, redirect
from .models import cartitem, products,orders
from django.db.models import Q


"""def carts(request):
    basket = cartitem.objects.all()
    get_subtotal = basket.subtotal()
    return render(request,'cart.html',
                  {'basket':basket,
                   'get_subtotal':get_subtotal})"""
def carts(request):
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
    })

def remove_from_cart(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(cartitem, id=product_id)
        product.delete()
        return redirect('carts')

def home(request):
    all_product = products.objects.all()
    return render(request,'home.html',{'all_product':all_product})

"""query = request.GET.get('query')
    if query:
        all_product = products.objects.filter(
            Q(name__icontains = query)|Q(description__icontains= query)
        )
    else:"""
    #return render(request,'home.html',{'all_product':all_product,'query':query})

            
            

    
            

    

def checkout(request):
    orderout = orders.objects.all()
    return render(request,'order.html',{'orderout':orderout})

"""def add_to_cart(request,product.id):
    if request.method == "POST":
        product = get_object_or_404(cartitem, id=product.id)
        product.add()
        return redirect('listings')"""

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

    return redirect('home')  # Or wherever you want


    
