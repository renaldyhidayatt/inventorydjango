from os import name
from django.urls import path

from .views import Categorylist, createCategory, deleteCategory, updateCategory

urlpatterns = [
    path("", Categorylist, name="category"),
    path("create/", createCategory, name="createcategory"),
    path("update/<int:id>", updateCategory, name="updatecategory"),
    path("delete/<int:id>", deleteCategory, name="deletecategory"),
]
