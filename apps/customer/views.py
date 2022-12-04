from django.shortcuts import render, redirect
from .models import Customer
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.


@login_required(login_url="/auth/login")
def customerList(request):
    customer = Customer.objects.all()

    context = {"customer": customer}
    print(customer)

    return render(request, "customer/index.html", context)


@login_required(login_url="/auth/login")
def customerCreate(request):
    if request.method == "POST":
        name = request.POST["name"]
        alamat = request.POST["alamat"]
        email = request.POST["email"]
        telepon = request.POST["telepon"]

        Customer.objects.create(name=name, alamat=alamat, email=email, telepon=telepon)

        messages.success(request, "Berhasil membuat customer")

        return redirect("customer")
    else:
        return render(request, "customer/create.html")


@login_required(login_url="/auth/login")
def customerUpdate(request, id):
    customer = Customer.objects.get(id=id)
    context = {"customer": customer}
    if request.method == "POST":
        name = request.POST["name"]
        alamat = request.POST["alamat"]
        email = request.POST["email"]
        telepon = request.POST["telepon"]

        customer.name = name
        customer.alamat = alamat
        customer.email = email
        customer.telepon = telepon

        customer.save()

        messages.success(request, "Berhasil membuat customer")

        return redirect("customer")
    else:
        return render(request, "customer/update.html", context)


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
