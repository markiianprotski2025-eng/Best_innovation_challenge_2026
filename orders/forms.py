from django import forms
from django.forms import ModelForm
from .models import Orders

class Orders_Form(ModelForm):
    class Meta:
        model = Orders
        fields = ['name', 'adress_order', 'priority', 'count_order']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'ПІБ(ФОП)',
            }),
            'adress_order': forms.TextInput(attrs={
                'placeholder': 'Адреса (місто, відділення або точна адреса)',
            }),
            'priority': forms.NumberInput(attrs={
                'placeholder': 'Оберіть пріоритетність',
            }),
            'count_order': forms.NumberInput(attrs={
                'placeholder': 'Кількість товару',
            }),
        }