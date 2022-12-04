from django.shortcuts import render, redirect
from .models import Category
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import csv
from django.contrib import messages


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
        messages.success(request, "Berhasil membuat category")

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

        messages.success(request, "Berhasil mengupdate category")

        return redirect("category")
    else:
        return render(request, "category/update.html", context)


@login_required(login_url="/auth/login")
def deleteCategory(request, id):
    category = Category.objects.get(id=id)

    try:
        category.delete()
        messages.success(request, "Berhasil mendelete category")

        return redirect("category")
    except Category.DoesNotExist:
        messages.error(request, "Error delete category")
        raise Exception("Category id not found")


@login_required(login_url="/auth/login")
def exportcategoryCsv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="Category.csv"'
    writer = csv.writer(response)
    writer.writerow(["Category Csv"])

    writer.writerow(["id", "name"])

    category = Category.objects.all().values_list("id", "name")

    for c in category:
        writer.writerow(c)

    return response
