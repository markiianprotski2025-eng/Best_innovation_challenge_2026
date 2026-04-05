from django.contrib import admin
from .models import Sklad, Product, Orders

admin.site.register(Sklad)
admin.site.register(Product)
admin.site.register(Orders)
