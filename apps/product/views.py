from typing import Optional, Any
from django.shortcuts import render, redirect
from .models import Product
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.category.models import Category
from apps.supplier.models import Supplier
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductForm


# Create your views here.
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name: str = "product/index.html"
    context_object_name: Optional[str] = "product"
    redirect_field_name: Any = "/auth/login"


class ProductCreateView(LoginRequiredMixin, View):
    redirect_field_name: Any = "/auth/login"

    def get(self, request):
        form = ProductForm()
        context = {"form": form}

        return render(request, "product/create.html", context)

    def post(self, request):
        form = ProductForm(request.POST, request.FILES or None)

        if form.is_valid():
            name = form.cleaned_data["name"]
            harga = form.cleaned_data["harga"]
            image = form.cleaned_data["image"]
            qty = form.cleaned_data["qty"]
            category = form.cleaned_data["category"]
            supplier = form.cleaned_data["supplier"]

            Product.objects.create(
                name=name,
                harga=harga,
                image=image,
                qty=int(qty),
                category=category,
                supplier=supplier,
            )
            messages.success(request, "Success create products")

            return redirect("product")
        else:
            messages.error(request, "Error field products")
            return redirect("product")


class ProductUpdateView(LoginRequiredMixin, View):
    redirect_field_name: Any = "/auth/login"

    def get(self, request, id):
        product = Product.objects.get(id=id)
        form = ProductForm(instance=product)

        context = {"form": form, "product": product}
        return render(request, "product/update.html", context)

    def post(self, request, id):
        product = Product.objects.get(id=id)

        form = ProductForm(request.POST, request.FILES or None)

        if form.is_valid():
            name = form.cleaned_data["name"]
            harga = form.cleaned_data["harga"]
            image = form.cleaned_data["image"]
            qty = form.cleaned_data["qty"]
            category = form.cleaned_data["category"]
            supplier = form.cleaned_data["supplier"]

            product.name = name
            product.harga = harga
            product.image = image
            product.qty = qty
            product.category = category
            product.supplier = supplier

            messages.success(request, "berhasil update product")

            return redirect("product")
        else:

            messages.error(request, "Error pada input product")
            return redirect("product")


@login_required(login_url="/auth/login")
def productDelete(request, id):
    product = Product.objects.get(id=id)

    try:
        product.delete()
        messages.success(request, "berhasil delete product")
        return redirect()
    except Product.DoesNotExist():
        messages.error(request, "Error pada product id")
        return redirect("product")
