from django.shortcuts import render
from .models import Sklad,Product

def orders(request):
    find_type = Sklad.objects.all()
    succes  = None
    eror = None
    adress_p = None

    if request.method == 'POST':
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
                                                'find_type':find_type})

