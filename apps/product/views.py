from django.shortcuts import render
from .models import Product
from apps.category.models import Category

# Create your views here.
def productList(request):
    product = Product.objects.all()

    context = {
        "product": product
    }

    return render(request, 'product/index.html', context)


def productCreate(request):
    if request.method == "POST":
        name = request.POST['POST']
        harga = request.POST['harga']
        image = request.FILES['image']
        qty = request.POST['qty']
        category = request.POST['category']

        category_id = Category.objects.get(nama=category)

        Product.objects.create(name=name,harga=harga,image=image,qty=qty,category=category)

        return redirect('product')
    else:
        return render(request,'product/create.html')

def productUpdate(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['POST']
        harga = request.POST['harga']
        image = request.FILES['image']
        qty = request.POST['qty']
        category = request.POST['category']

        product.name = name
        product.harga = harga
        product.image = image
        product.qty = qty
        product.category = category

        return redirect('product')
    else:
        return render(request, 'product/update.html')


def productDelete(request, id):
    product = Product.objects.get(id=id)

    try:
        product.delete()
        return redirect()
    except Product.DoesNotExist():
        raise Exception("Tolol")
