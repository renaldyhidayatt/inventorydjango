from django.shortcuts import render, redirect
from .models import Category
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/auth/login")
def Categorylist(request):
    categories = Category.objects.all()

    context = {"categories": categories}

    return render(request, "category/index.html", context)


@login_required(login_url="/auth/login")
def createCategory(request):
    if request.method == "POST":
        name = request.POST["name"]

        Category.objects.create(name=name)

        return redirect("category")
    else:
        return render(request, "category/create.html")


@login_required(login_url="/auth/login")
def updateCategory(request, id):
    category = Category.objects.get(id=id)
    context = {"category": category}
    if request.method == "POST":
        name = request.POST["name"]

        category.name = name

        category.save()

        return redirect("category")
    else:
        return render(request, "category/update.html", context)


@login_required(login_url="/auth/login")
def deleteCategory(request, id):
    category = Category.objects.get(id=id)

    try:
        category.delete()

        return redirect("category")
    except Category.DoesNotExist:
        raise Exception("Category id not found")
