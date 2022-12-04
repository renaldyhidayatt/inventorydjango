from django.shortcuts import render, redirect
from .models import Product
from apps.category.models import Category
from apps.supplier.models import Supplier
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required(login_url="/auth/login")
def productList(request):
    product = Product.objects.all()

    context = {"product": product}

    return render(request, "product/index.html", context)


@login_required(login_url="/auth/login")
def productCreate(request):
    category = Category.objects.all()
    supplier = Supplier.objects.all()
    context = {"category": category, "supplier": supplier}
    if request.method == "POST":
        name = request.POST["name"]
        harga = request.POST["harga"]
        image = request.FILES.get("image")
        qty = request.POST.get("qty")
        category = request.POST["category"]
        supplier = request.POST["supplier"]

        category_id = Category.objects.get(id=category)
        supplier_id = Supplier.objects.get(id=supplier)

        if not category_id:
            messages.info(request, "required category id")
            return redirect("product")

        if not supplier_id:
            messages.info(request, "required supplier id")
            return redirect("product")

        Product.objects.create(
            name=name,
            harga=harga,
            image=image,
            qty=int(qty),
            category=category_id,
            supplier=supplier_id,
        )
        messages.success(request, "berhasil membuat product")

        return redirect("product")
    else:
        return render(request, "product/create.html", context)


@login_required(login_url="/auth/login")
def productUpdate(request, id):
    product = Product.objects.get(id=id)
    category = Category.objects.all()
    supplier = Supplier.objects.all()
    context = {"product": product, "category": category, "supplier": supplier}
    if request.method == "POST":
        name = request.POST["name"]
        harga = request.POST["harga"]
        qty = request.POST.get("qty")
        category = request.POST["category"]
        supplier = request.POST["supplier"]

        category_id = Category.objects.get(id=category)
        supplier_id = Supplier.objects.get(id=supplier)

        if not category_id:
            messages.info(request, "required category id")
            return redirect("product")

        if not supplier_id:
            messages.info(request, "required supplier id")
            return redirect("product")

        product.name = name
        product.harga = harga
        product.qty = int(qty)
        product.category = category_id

        product.save()

        messages.success(request, "berhasil update product")

        return redirect("product")
    else:
        return render(request, "product/update.html", context)


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
