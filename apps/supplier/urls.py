from django.urls import path
from .views import supplierList, supplierCreate, supplierUpdate, supplierDelete


urlpatterns = [
    path("", supplierList, name="supplier"),
    path("create/", supplierCreate, name="suppliercreate"),
    path("update/<int:id>", supplierUpdate, name="supplierupdate"),
    path("delete/<int:id>", supplierDelete, name="supplierdelete"),
]
