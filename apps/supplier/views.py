from django.shortcuts import render, redirect

from .models import Supplier
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/auth/login")
def supplierList(request):
    supplier = Supplier.objects.all()

    context = {"supplier": supplier}

    return render(request, "supplier/index.html", context)


@login_required(login_url="/auth/login")
def supplierCreate(request):
    if request.method == "POST":
        name = request.POST["name"]
        alamat = request.POST["alamat"]
        email = request.POST["email"]
        telepon = request.POST["telepon"]

        Supplier.objects.create(name=name, alamat=alamat, email=email, telepon=telepon)

        return redirect("supplier")

    else:
        return render(request, "supplier/create.html")


@login_required(login_url="/auth/login")
def supplierUpdate(request, id):
    supplier = Supplier.objects.get(id=id)
    context = {"supplier": supplier}
    if request.method == "POST":
        name = request.POST["name"]
        alamat = request.POST["alamat"]
        email = request.POST["email"]
        telepon = request.POST["telepon"]

        supplier.name = name
        supplier.alamat = alamat
        supplier.email = email
        supplier.telepon = telepon

        supplier.save()

        return redirect("supplier")

    else:
        return render(request, "supplier/update.html", context)


@login_required(login_url="/auth/login")
def supplierDelete(request, id):
    supplier = Supplier.objects.get(id=id)

    try:
        supplier.delete()

        return redirect("sale")
    except Supplier.DoesNotExist:
        raise Exception("Errooror")
