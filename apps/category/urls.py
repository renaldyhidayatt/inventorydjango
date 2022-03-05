from django.urls import path

from .views import categorylist

urlpatterns = [path("", categorylist, name="categorylist")]
