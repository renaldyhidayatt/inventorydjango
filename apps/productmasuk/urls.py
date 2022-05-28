from os import name
from django.urls import path
from .views import prodmasuk, prodmasukCreate, prodmasukUpdate, prodmasukDelete

urlpatterns = [
    path("", prodmasuk, name="productmasuk"),
    path("create/", prodmasukCreate, name="prodmasukcreate"),
    path("update/<int:id>", prodmasukUpdate, name="prodmasukupdate"),
    path("delete/<int:id>", prodmasukDelete, name="prodmasukdelete")
]