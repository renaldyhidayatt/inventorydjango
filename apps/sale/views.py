from django.shortcuts import render, redirect
from .models import Sale
from apps.product.models import Product
from apps.customer.models import Customer
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/auth/login")
def saleList(request):
    sale = Sale.objects.all()

    context = {"sale": sale}

    return render(request, "sale/index.html", context)


@login_required(login_url="/auth/login")
def saleCreate(request):
    product = Product.objects.all()
    customer = Customer.objects.all()

    context = {"product": product, "customer": customer}
    if request.method == "POST":
        product_id = request.POST["product"]
        customer_id = request.POST["customer"]
        qty = request.POST["qty"]
        date_transaksi = request.POST["date_transaksi"]

        product = Product.objects.get(id=product_id)
        customer = Customer.objects.get(id=customer_id)

        if not product:
            messages.error(request, "required product ")
            return redirect("sale")

        if not customer:
            messages.error(request, "required customer")
            return redirect("sale")

        quantityproduct = int(product.qty) - int(qty)
        product.qty = quantityproduct

        harga = int(qty) * int(product.harga)

        product.save()

        Sale.objects.create(
            customer=customer,
            product=product,
            qty=int(qty),
            total_price=harga,
            date_transaksi=date_transaksi,
        )
        messages.success(request, "Berhasil membuat sale")
        return redirect("sale")

    else:
        return render(request, "sale/create.html", context=context)


@login_required(login_url="/auth/login")
def saleUpdate(request, id):
    sale = Sale.objects.get(id=id)
    product = Product.objects.all()
    customer = Customer.objects.all()
    context = {"sale": sale, "product": product, "customer": customer}
    if request.method == "POST":
        product_id = request.POST["product"]
        customer_id = request.POST["customer"]
        qty = request.POST["qty"]
        date_transaksi = request.POST["date_transaksi"]

        product = Product.objects.get(id=product_id)
        customer = Customer.objects.get(id=customer_id)

        if not product:
            messages.error(request, "undefined id product ")
            return redirect("sale")

        if not customer:
            messages.error(request, "undefined id customer")
            return redirect("sale")

        quantityproduct = int(product.qty) - int(qty)
        product.qty = quantityproduct

        harga = int(qty) * int(product.harga)

        product.save()

        sale.customer = customer
        sale.product = product
        sale.qty = qty
        sale.date_transaksi = date_transaksi
        sale.total_price = harga

        sale.save()
        messages.success(request, "berhasil update sale")

        return redirect("sale")

    else:
        return render(request, "sale/update.html", context)


@login_required(login_url="/auth/login")
def saleDelete(request, id):
    sale = Sale.objects.get(id=id)

    try:
        sale.delete()
        messages.success(request, "berhasil mendelete sale")

        return redirect("sale")
    except Sale.DoesNotExist:
        messages.error(request, "failed delete sale")

        return redirect("sale")


@login_required(login_url="/auth/login")
def saleGeneratePdf(request, id):
    sale = Sale.objects.get(id=id)

    try:
        template_path = "sale/generatePdf.html"
        context = {"sale": sale}
        response = HttpResponse(content_type="application/pdf")

        response["Content-Disposition"] = 'filename="report.pdf"'

        template = get_template(template_path)
        html = template.render(context)

        pdf = pisa.CreatePDF(html, dest=response)

        if pdf.err:
            return HttpResponse("We had some errors <pre>" + html + "</pre>")

        return response

    except Sale.DoesNotExist:
        messages.error(request, "failed get id sale")

        return redirect("sale")
