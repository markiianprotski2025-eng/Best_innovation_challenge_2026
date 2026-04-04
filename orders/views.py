from django.shortcuts import render
from .models import Sklad,Product,Orders
from .forms import Orders_Form
from django.http import JsonResponse


def orders(request):
    user_order = Orders.objects.filter(user = request.user)
    succes  = None
    eror = None
    adress_p = None
    adress_order = None
    id = None

    


    return render(request,'orders/orders.html',{'user_order':user_order})

    '''if request.method == 'POST':
        product = request.POST.get('promo')
        find_product  = Product.objects.filter(name__iexact=product).first()
        if find_product:
            succes = find_product.count
            adress_p = find_product.sklad.adress
        else:
            eror = 'немає такого товару'
    return render(request,'orders/orders.html',{
                                                'error':eror,
                                                'succes':succes,
                                                'adress_p':adress_p,
                                                'find_type':find_type})'''


def create_order(request):
    form = Orders_Form()
    sklads = Sklad.objects.all()

    if request.method == 'POST':
        form = Orders_Form(request.POST)
        product_id = request.POST.get('product_id')
        
        if form.is_valid() and product_id:
            order = form.save(commit=False)
            order.user = request.user
            order.product = Product.objects.get(id=product_id)
            order.save()
        # якщо product_id пустий — форма просто перерендериться з помилкою

    return render(request, 'orders/checkout.html', {'form': form, 'sklads': sklads})


def get_products(request):
    sklad_id = request.GET.get('sklad_id')
    products = Product.objects.filter(sklad_id=sklad_id).values('id', 'name')
    return JsonResponse(list(products), safe=False)