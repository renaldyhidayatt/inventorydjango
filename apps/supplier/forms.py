from django import forms
from .models import Supplier


class SupplierForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    alamat = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    telepon = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "custom-file-input"})
    )

    class Meta:
        model = Supplier
        fields = ["name", "alamat", "email", "telepon", "image"]
