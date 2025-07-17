# forms.py
from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class ChangePriceForm(forms.Form):
    new_price = forms.DecimalField(label="Новая цена", min_value=0)

class PriceForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    new_price = forms.DecimalField(max_digits=10, decimal_places=2)