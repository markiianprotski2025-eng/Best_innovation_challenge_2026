from django.urls import path
from . import views
urlpatterns = [
    path('',views.orders,name="orders"),
    path('checkout/',views.create_order,name='checkout' ),
    path('get-products/', views.get_products, name='get_products'),

]