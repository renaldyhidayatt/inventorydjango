from django.shortcuts import redirect, render

from apps.product.models import Product
from apps.supplier.models import Supplier
from .models import ProductMasuk
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/auth/login")
def prodmasuk(request):
    productmasuk = ProductMasuk.objects.all()

    context = {"productmasuk": productmasuk}

    return render(request, "productmasuk/index.html", context)


@login_required(login_url="/auth/login")
def prodmasukCreate(request):
    product = Product.objects.all()
    supplier = Supplier.objects.all()

    context = {"product": product, "supplier": supplier}

    if request.method == "POST":
        qty = request.POST["qty"]
        tanggal = request.POST["tanggal"]
        product = request.POST["product"]
        supplier = request.POST["supplier"]

        product_id = Product.objects.get(name=product)
        supplier_id = Supplier.objects.get(name=supplier)

        ProductMasuk.objects.create(
            qty=qty, tanggal=tanggal, product=product_id, supplier=supplier_id
        )

        return redirect("productmasuk")
    else:
        return render(request, "productmasuk/create.html", context)


@login_required(login_url="/auth/login")
def prodmasukUpdate(request, id):
    product = Product.objects.all()
    supplier = Supplier.objects.all()
    productmasuk = ProductMasuk.objects.get(id=id)

    context = {"product": product, "supplier": supplier, "productmasuk": productmasuk}

    if request.method == "POST":
        qty = request.POST["qty"]
        tanggal = request.POST["tanggal"]
        product = request.POST["product"]
        supplier = request.POST["supplier"]

        product_id = Product.objects.get(name=product)
        supplier_id = Supplier.objects.get(name=supplier)

        productmasuk.qty = qty
        productmasuk.tanggal = tanggal
        productmasuk.product = product_id
        productmasuk.supplier = supplier_id

        productmasuk.save()

        return redirect("productmasuk")
    else:
        return render(request, "productmasuk/update.html", context)


@login_required(login_url="/auth/login")
def prodmasukDelete(request, id):
    productmasuk = ProductMasuk.objects.get(id=id)

    try:
        productmasuk.delete()
        return redirect("productmasuk")
    except ProductMasuk.DoesNotExist:
        raise Exception("Error")
