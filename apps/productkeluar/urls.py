from django.urls import path
from .views import productkeluar, prodkeluarCreate, prodkeluarUpdate, prodkeluarDelete

urlpatterns = [
    path("", productkeluar, name="productkeluar"),
    path("create/", prodkeluarCreate, name="prodkeluarcreate"),
    path("update/<int:id>", prodkeluarUpdate, name="prodkeluarupdate"),
    path("delete/<int:id>", prodkeluarDelete, name="prodkeluardelete"),
]