from django import forms
from .models import Product
from apps.category.models import Category
from apps.supplier.models import Supplier


class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    harga = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    image = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "custom-file-input"})
    )
    qty = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    supplier = forms.ModelChoiceField(
        queryset=Supplier.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Product
        fields = ["name", "harga", "image", "qty", "category", "supplier"]
