from django.shortcuts import render
from apps.customer.models import Customer
from apps.product.models import Product
from apps.supplier.models import Supplier
from apps.sale.models import Sale
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/auth/login")
def dashboard(request):

    customer = Customer.objects.all().count()
    product = Product.objects.all().count()
    supplier = Supplier.objects.all().count()
    sale = Sale.objects.all().count()

    context = {
        "customer": customer,
        "product": product,
        "supplier": supplier,
        "sale": sale,
    }

    return render(request, "index.html", context)
