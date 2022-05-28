from django.shortcuts import render, redirect
from .models import Product
from apps.category.models import Category
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/auth/login")
def productList(request):
    product = Product.objects.all()

    context = {"product": product}

    return render(request, "product/index.html", context)


@login_required(login_url="/auth/login")
def productCreate(request):
    category = Category.objects.all()
    context = {"category": category}
    if request.method == "POST":
        name = request.POST["name"]
        harga = request.POST["harga"]
        image = request.FILES.get("image")
        qty = request.POST.get("qty")
        category = request.POST["category"]

        category_id = Category.objects.get(name=category)

        Product.objects.create(
            name=name, harga=harga, image=image, qty=qty, category=category_id
        )

        return redirect("product")
    else:
        return render(request, "product/create.html", context)


@login_required(login_url="/auth/login")
def productUpdate(request, id):
    product = Product.objects.get(id=id)
    category = Category.objects.all()
    context = {"product": product, "category": category}
    if request.method == "POST":
        name = request.POST["name"]
        harga = request.POST["harga"]
        image = request.FILES["image"]
        qty = request.POST.get("qty")
        category = request.POST["category"]

        category_id = Category.objects.get(name=category)

        product.name = name
        product.harga = harga
        product.image = image
        product.qty = qty
        product.category = category_id

        return redirect("product")
    else:
        return render(request, "product/update.html", context)


@login_required(login_url="/auth/login")
def productDelete(request, id):
    product = Product.objects.get(id=id)

    try:
        product.delete()
        return redirect()
    except Product.DoesNotExist():
        raise Exception("Doesn't  error model Product")
