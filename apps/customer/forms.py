from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    alamat = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    telepon = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control"}))

    class Meta:
        model = Customer
        fields = ["name", "alamat", "email", "telepon"]
