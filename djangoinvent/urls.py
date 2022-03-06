"""djangoinvent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("apps.users.authurls")),
    path("category/", include("apps.category.urls")),
    path("customer/", include("apps.customer.urls")),
    path("product/", include("apps.product.urls")),
    path("sale/", include("apps.sale.urls")),
    path("supplier/", include("apps.supplier.urls")),
    path("productmasuk/", include("apps.productmasuk.urls")),
    path("productkeluar/", include("apps.productkeluar.urls")),
    path("", include("apps.dashboard.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "apps.handler.page404.page_not_found_view"
