from django.urls import path

from .views import customerList, customerCreate, customerDelete, customerUpdate

urlpatterns = [
    path("", customerList, name="customer"),
    path("create/", customerCreate, name="createcustomer"),
    path("update/<int:id>", customerUpdate, name="updatecustomer"),
    path("delete/<int:id>", customerDelete, name="deletecustomer"),
]
