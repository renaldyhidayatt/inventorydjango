from typing import Optional, Any
from django.shortcuts import render, redirect
from .models import Category
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import csv
from django.views.generic import View, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import CategoryForm

# Create your views here.


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name: str = "category/index.html"
    context_object_name: Optional[str] = "categories"
    redirect_field_name = "/auth/login"


class CategoryCreateView(LoginRequiredMixin, View):
    redirect_field_name: Any = "/auth/login"

    def get(self, request):
        form = CategoryForm()

        context = {"form": form}
        return render(request, "category/create.html", context)

    def post(self, request):
        form = CategoryForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]

            Category.objects.create(name=name)

            messages.success(request, "Berhasil membuat Category")

            return redirect("category")
        else:
            messages.error(request, "Error input category")
            return redirect("category")


class CategoryUpdateView(LoginRequiredMixin, View):
    redirect_field_name: Any = "/auth/login"

    def get(self, request, id):
        category = Category.objects.get(id=id)
        form = CategoryForm(instance=category)

        context = {"form": form, "category": category}

        return render(request, "category/update.html", context)

    def post(self, request, id):
        form = CategoryForm()
        category = Category.objects.get(id=id)

        if form.is_valid():
            name = form.cleaned_data["name"]

            category.name = name

            category.save()

            messages.success(request, "Berhasil mengupdate category")

            return redirect("category")
        else:
            messages.error(request, "Error input category")
            return redirect("category")


class CategoryDeleteView(LoginRequiredMixin, View):
    def get(request, id):
        category = Category.objects.get(id=id)

        try:
            category.delete()
            messages.success(request, "Berhasil mendelete category")

            return redirect("category")
        except Category.DoesNotExist:
            messages.error(request, "Error delete category")
            return redirect("category")


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
