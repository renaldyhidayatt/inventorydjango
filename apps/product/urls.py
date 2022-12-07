from django.urls import path
from .views import ProductListView, ProductCreateView, ProductUpdateView, productDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(
        "",
        login_required(ProductListView.as_view(), login_url="/auth/login"),
        name="product",
    ),
    path(
        "create/",
        login_required(ProductCreateView.as_view(), login_url="/auth/login"),
        name="productcreate",
    ),
    path(
        "update/<int:id>",
        login_required(ProductUpdateView.as_view(), login_url="/auth/login"),
        name="productupdate",
    ),
    path("delete/<int:id>", productDelete, name="productdelete"),
]
