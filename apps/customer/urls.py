from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    CustomerListView,
    CustomerCreateView,
    CustomerUpdateView,
    customerDelete,
)

urlpatterns = [
    path(
        "",
        login_required(CustomerListView.as_view(), login_url="/auth/login"),
        name="customer",
    ),
    path(
        "create/",
        login_required(CustomerCreateView.as_view(), login_url="/auth/login"),
        name="createcustomer",
    ),
    path(
        "update/<int:id>",
        login_required(CustomerUpdateView.as_view(), login_url="/auth/login"),
        name="updatecustomer",
    ),
    path("delete/<int:id>", customerDelete, name="deletecustomer"),
]
