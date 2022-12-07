from django import forms
from .models import Sale
from apps.customer.models import Customer
from apps.product.models import Product


class SaleForm(forms.ModelForm):
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    qty = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    date_transaksi = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"})
    )

    class Meta:
        model = Sale
        fields = ["customer", "product", "qty", "date_transaksi"]
