from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Category
        fields = ["name"]
