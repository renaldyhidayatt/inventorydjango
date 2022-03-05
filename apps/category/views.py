from django.shortcuts import render, redirect
from .models import Category

# Create your views here.


def Categorylist(request):
    categories = Category.objects.all()

    context = {"category": categories}

    return render(request, "category/index.html", context)


def createCategory(request):
    if request.method == "POST":
        name = request.POST["name"]

        Category.objects.create(name=name)

        return redirect("category")
    else:
        return render(request, "category/create.html")


def updateCategory(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST["name"]

        category.name = name

        category.save()

        return redirect('category')
    else:
        return render(request, 'category/update.html')



def deleteCategory(request,id):
    category = Category.objects.get(id=id)

    try:
        category.delete()

        return redirect('category')
    except Category.DoesNotExist:
        raise Exception("Category id not found")
        




