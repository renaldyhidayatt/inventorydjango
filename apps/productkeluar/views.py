from django.shortcuts import redirect, render

from apps.customer.models import Customer
from apps.product.models import Product
from .models import ProductKeluar
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/auth/login")
def productkeluar(request):
    productkeluar = ProductKeluar.objects.all()

    context = {"productkeluar": productkeluar}

    return render(request, "productkeluar/index.html", context)


@login_required(login_url="/auth/login")
def prodkeluarCreate(request):
    product = Product.objects.all()
    customer = Customer.objects.all()

    context = {"product": product, "customer": customer}

    if request.method == "POST":
        qty = request.POST.get("qty")
        tanggal = request.POST.get("tanggal")
        product = request.POST.get("product")
        customer = request.POST.get("customer")

        product_id = Product.objects.get(name=product)
        customer_id = Customer.objects.get(name=customer)

        ProductKeluar.objects.create(
            qty=qty, tanggal=tanggal, product=product_id, customer=customer_id
        )

        return redirect("productkeluar")
    else:
        return render(request, "productkeluar/create.html", context)


@login_required(login_url="/auth/login")
def prodkeluarUpdate(request, id):
    productkeluar = ProductKeluar.objects.get(id=id)
    product = Product.objects.all()
    customer = Customer.objects.all()

    context = {"productkeluar": productkeluar, "product": product, "customer": customer}

    if request.method == "POST":
        qty = request.POST.get("qty")
        tanggal = request.POST.get("tanggal")
        product = request.POST.get("product")
        customer = request.POST.get("customer")

        product_id = Product.objects.get(name=product)
        customer_id = Customer.objects.get(name=customer)

        productkeluar.qty = qty
        productkeluar.tanggal = tanggal
        productkeluar.product = product_id
        productkeluar.customer = customer_id

        productkeluar.save()

        return redirect("productkeluar")
    else:
        return render(request, "productkeluar/update.html", context)


@login_required(login_url="/auth/login")
def prodkeluarDelete(request, id):
    productkeluar = ProductKeluar.objects.get(id=id)

    try:
        productkeluar.delete()

        return redirect("productkeluar")
    except ProductKeluar.DoesNotExist:
        raise Exception("Error")
