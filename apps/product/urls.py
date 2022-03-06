from django.urls import path
from .views import productList, productCreate, productUpdate, productDelete

urlpatterns = [
    path("", productList, name="product"),
    path("create/", productCreate, name="productcreate"),
    path("update/<int:id>", productUpdate, name="productupdate"),
    path("delete/<int:id>", productList, name="productdelete"),
]
