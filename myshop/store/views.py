# store/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Product, CartItem, Order

def product_list(request):
    products = Product.objects.all()[:10] # Hard limit to 10 products
    return render(request, 'store/product_list.html', {'products': products})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'store/cart_detail.html', {'cart_items': cart_items, 'total': total})

@login_required
def mpesa_checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    
    if request.method == 'POST':
        phone = request.POST.get('phone_number')
        # 1. Create the simulated order
        Order.objects.create(user=request.user, phone_number=phone, total_amount=total)
        # 2. Clear the cart
        cart_items.delete()
        # 3. Redirect to success
        return render(request, 'store/success.html')

    return render(request, 'store/checkout.html', {'total': total})