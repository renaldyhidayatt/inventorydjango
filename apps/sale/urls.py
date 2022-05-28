from django.urls import path
from .views import saleList, saleCreate, saleUpdate, saleDelete


urlpatterns = [
    path("", saleList, name="sale"),
    path("create/", saleCreate, name="salecreate"),
    path("update/<int:id>", saleUpdate, name="saleupdate"),
    path("delete/<int:id>", saleDelete, name="saledelete"),
]