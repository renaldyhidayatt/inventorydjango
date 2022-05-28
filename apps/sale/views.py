from django.shortcuts import render, redirect
from .models import Sale
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/auth/login")
def saleList(request):
    sale = Sale.objects.all()

    context = {"sale": sale}

    return render(request, "sale/index.html", context)


@login_required(login_url="/auth/login")
def saleCreate(request):
    if request.method == "POST":
        name = request.POST["name"]
        alamat = request.POST["alamat"]
        email = request.POST["email"]
        telepon = request.POST["telepon"]

        Sale.objects.create(name=name, alamat=alamat, email=email, telepon=telepon)

        return redirect("sale")

    else:
        return render(request, "sale/create.html")


@login_required(login_url="/auth/login")
def saleUpdate(request, id):
    sale = Sale.objects.get(id=id)
    context = {"sale": sale}
    if request.method == "POST":
        name = request.POST["name"]
        alamat = request.POST["alamat"]
        email = request.POST["email"]
        telepon = request.POST["telepon"]

        sale.name = name
        sale.alamat = alamat
        sale.email = email
        sale.telepon = telepon

        sale.save()

        return redirect("sale")

    else:
        return render(request, "sale/update.html", context)


@login_required(login_url="/auth/login")
def saleDelete(request, id):
    sale = Sale.objects.get(id=id)

    try:
        sale.delete()

        return redirect("sale")
    except Sale.DoesNotExist:
        raise Exception("Errooror")
