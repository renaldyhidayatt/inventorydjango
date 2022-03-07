from django.urls import path

from .views import (
    Categorylist,
    createCategory,
    deleteCategory,
    updateCategory,
    exportcategoryCsv,
)

urlpatterns = [
    path("", Categorylist, name="category"),
    path("create/", createCategory, name="createcategory"),
    path("update/<int:id>", updateCategory, name="updatecategory"),
    path("delete/<int:id>", deleteCategory, name="deletecategory"),
    path("export/", exportcategoryCsv, name="exportcategory"),
]
