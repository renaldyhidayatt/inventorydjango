from typing import Optional, Any
from django.shortcuts import render, redirect
from .models import Customer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import View, ListView
from .forms import CustomerForm


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name: str = "customer/index.html"
    context_object_name: Optional[str] = "customer"
    redirect_field_name: Any = "/auth/login"


class CustomerCreateView(LoginRequiredMixin, View):
    redirect_field_name: Any = "/auth/login"

    def get(self, request):
        form = CustomerForm()
        context = {"form": form}
        return render(request, "customer/create.html", context)

    def post(self, request):
        form = CustomerForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            alamat = form.cleaned_data["alamat"]
            email = form.cleaned_data["email"]
            telepon = form.cleaned_data["telepon"]
            Customer.objects.create(
                name=name, alamat=alamat, email=email, telepon=telepon
            )

            messages.success(request, "Berhasil membuat customer")

            return redirect("customer")
        else:
            messages.error(request, "Error input customer")
            return redirect("customer")


class CustomerUpdateView(LoginRequiredMixin, View):
    redirect_field_name: Any = "/auth/login"

    def get(self, request, id):
        customer = Customer.objects.get(id=id)
        form = CustomerForm(instance=customer)

        context = {"form": form, "customer": customer}

        return render(request, "customer/update.html", context)

    def post(self, request, id):
        form = CustomerForm()
        customer = Customer.objects.get(id=id)

        if form.is_valid():
            name = form.cleaned_data["name"]
            alamat = form.cleaned_data["alamat"]
            email = form.cleaned_data["email"]
            telepon = form.cleaned_data["telepon"]

            customer.name = name
            customer.alamat = alamat
            customer.email = email
            customer.telepon = telepon

            customer.save()
            messages.success(request, "Berhasil mengupdate customer")

            return redirect("customer")
        else:
            messages.error(request, "Error pada input customer")
            return redirect("customer")


@login_required(login_url="/auth/login")
def customerDelete(request, id):
    customer = Customer.objects.get(id=id)

    try:
        customer.delete()
        messages.success(request, "Berhasil mendelete customer")

        return redirect("customer")
    except Customer.DoesNotExist:
        messages.error(request, "Error Pada delete customer")

        return redirect("customer")
