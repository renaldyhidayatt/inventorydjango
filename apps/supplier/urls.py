from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    SupplierListView,
    SupplierCreateView,
    SupplierUpdateView,
    supplierDelete,
)


urlpatterns = [
    path(
        "",
        login_required(SupplierListView.as_view(), login_url="/auth/login"),
        name="supplier",
    ),
    path(
        "create/",
        login_required(SupplierCreateView.as_view(), login_url="/auth/login"),
        name="suppliercreate",
    ),
    path(
        "update/<int:id>",
        login_required(SupplierUpdateView.as_view(), login_url="/auth/login"),
        name="supplierupdate",
    ),
    path("delete/<int:id>", supplierDelete, name="supplierdelete"),
]
