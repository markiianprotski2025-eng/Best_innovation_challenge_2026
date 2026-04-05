from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Sklad, Product, Orders
from .forms import Orders_Form

@login_required(login_url='login')
def orders(request):
    user_order = Orders.objects.filter(user=request.user).select_related('product__sklad')
    return render(request, 'orders/orders.html', {'user_order': user_order})


@login_required(login_url='login')
def create_order(request):
    form = Orders_Form()
    sklads = Sklad.objects.all()

    if request.method == 'POST':
        form = Orders_Form(request.POST)
        product_id = request.POST.get('product_id')
        
        if form.is_valid() and product_id:
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                product = None

            if product:
                order = form.save(commit=False)
                order.user = request.user
                order.product = product
                order.save()
                return redirect('orders')

    return render(request, 'orders/checkout.html', {'form': form, 'sklads': sklads})



@login_required(login_url='login')
def get_products(request):
    sklad_id = request.GET.get('sklad_id')
    if not sklad_id:
        return JsonResponse([], safe=False)

    products = Product.objects.filter(sklad_id=sklad_id).values('id', 'name', 'price', 'count', 'sklad__adress')
    return JsonResponse(list(products), safe=False)