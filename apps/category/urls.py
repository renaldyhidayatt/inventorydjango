from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (
    CategoryListView,
    CategoryCreateView,
    CategoryDeleteView,
    CategoryUpdateView,
    exportcategoryCsv,
)

urlpatterns = [
    path(
        "",
        login_required(CategoryListView.as_view(), login_url="/auth/login"),
        name="category",
    ),
    path(
        "create/",
        login_required(CategoryCreateView.as_view(), login_url="/auth/login"),
        name="createcategory",
    ),
    path(
        "update/<int:id>",
        login_required(CategoryUpdateView.as_view(), login_url="/auth/login"),
        name="updatecategory",
    ),
    path(
        "delete/<int:id>",
        login_required(CategoryDeleteView, login_url="/auth/login"),
        name="deletecategory",
    ),
    path("export/", exportcategoryCsv, name="exportcategory"),
]
