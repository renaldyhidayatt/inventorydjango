from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    SaleListView,
    SaleCreateView,
    SaleUpdateView,
    saleDelete,
    saleGeneratePdf,
)


urlpatterns = [
    path(
        "", login_required(SaleListView.as_view(), login_url="/auth/login"), name="sale"
    ),
    path(
        "create/",
        login_required(SaleCreateView.as_view(), login_url="/auth/login"),
        name="salecreate",
    ),
    path(
        "update/<int:id>",
        login_required(SaleUpdateView.as_view(), login_url="/auth/login"),
        name="saleupdate",
    ),
    path("delete/<int:id>", saleDelete, name="saledelete"),
    path("generatepdf/<int:id>", saleGeneratePdf, name="generatepdf"),
]
