from typing import Optional, Any
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Supplier
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SupplierForm

# Create your views here.
class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name: str = "supplier/index.html"
    context_object_name: Optional[str] = "supplier"
    redirect_field_name: Any = "/auth/login"


class SupplierCreateView(LoginRequiredMixin, View):
    redirect_field_name: Any = "/auth/login"

    def get(self, request):
        form = SupplierForm()
        context = {"form": form}
        return render(request, "supplier/create.html", context)

    def post(self, request):
        form = SupplierForm(request.POST, request.FILES or None)

        if form.is_valid():
            name = form.cleaned_data["name"]
            alamat = form.cleaned_data["alamat"]
            email = form.cleaned_data["email"]
            telepon = form.cleaned_data["telepon"]
            image = form.cleaned_data["image"]

            Supplier.objects.create(
                name=name, alamat=alamat, email=email, telepon=telepon, image=image
            )

            messages.success(request, "Success create supplier")

            return redirect("supplier")
        else:
            messages.error(request, "Error field supplier")
            return redirect("supplier")


class SupplierUpdateView(LoginRequiredMixin, View):
    def get(self, request, id):
        supplier = Supplier.objects.get(id=id)
        form = SupplierForm(instance=supplier)

        context = {"supplier": supplier, "form": form}

        return render(request, "supplier/update.html", context)

    def post(self, request, id):
        supplier = Supplier.objects.get(id=id)
        form = SupplierForm(request.POST, request.FILES or None)

        if form.is_valid():
            name = form.cleaned_data["name"]
            alamat = form.cleaned_data["alamat"]
            email = form.cleaned_data["email"]
            telepon = form.cleaned_data["telepon"]
            image = form.cleaned_data["image"]

            supplier.name = name
            supplier.alamat = alamat
            supplier.email = email
            supplier.telepon = telepon
            supplier.image = image

            supplier.save()

            messages.success(request, "berhasil update suppkier")

            return redirect("supplier")
        else:

            messages.error(request, "error pada input supplier")
            return redirect("supplier")


@login_required(login_url="/auth/login")
def supplierDelete(request, id):
    supplier = Supplier.objects.get(id=id)

    try:
        supplier.delete()

        return redirect("sale")
    except Supplier.DoesNotExist:
        raise Exception("Errooror")
