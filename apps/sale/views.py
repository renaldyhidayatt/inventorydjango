from typing import Optional, Any
from django.shortcuts import render, redirect
from .models import Sale
from apps.product.models import Product
from apps.customer.models import Customer
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from xhtml2pdf import pisa
from .forms import SaleForm
from django.contrib.auth.decorators import login_required


# Create your views here.
class SaleListView(LoginRequiredMixin, ListView):
    model = Sale
    template_name: str = "sale/index.html"
    context_object_name: Optional[str] = "sale"
    redirect_field_name: Any = "/auth/login"


class SaleCreateView(LoginRequiredMixin, View):
    redirect_field_name: Any = "/auth/login"

    def get(self, request):
        form = SaleForm()

        context = {"form": form}

        return render(request, "sale/create.html", context)

    def post(self, request):
        form = SaleForm(request.POST, request.FILES or None)

        if form.is_valid():
            product = form.cleaned_data["product"]
            customer = form.cleaned_data["customer"]
            qty = form.cleaned_data["qty"]
            date_transaksi = form.cleaned_data["date_transaksi"]

            product_id = Product.objects.get(name=product)

            if not product_id:
                messages.error(request, "required product")
                return redirect("sale")

            quantityproduct = int(product_id.qty) - int(qty)
            product_id.qty = quantityproduct

            harga = int(qty) * int(product_id.harga)

            product_id.save()

            Sale.objects.create(
                customer=customer,
                product=product_id,
                qty=int(qty),
                total_price=harga,
                date_transaksi=date_transaksi,
            )
            messages.success(request, "Berhasil membuat sale")
            return redirect("sale")
        else:
            messages.error(request, "Error input Sale")
            return redirect("sale")


class SaleUpdateView(LoginRequiredMixin, View):
    redirect_field_name: Any = "/auth/login"

    def get(self, request, id):
        sale = Sale.objects.get(id=id)
        form = SaleForm(instance=sale)

        context = {"form": form, "sale": sale}

        return render(request, "sale/update.html", context)

    def post(self, request, id):
        sale = Sale.object.get(id=id)
        form = SaleForm(request.POST, request.FILES or None)
        if form.is_valid():
            product = form.cleaned_data["product"]
            customer = form.cleaned_data["customer"]
            qty = form.cleaned_data["qty"]
            date_transaksi = form.cleaned_data["date_transaksi"]

            product_id = Product.objects.get(name=product)

            if not product_id:
                messages.error(request, "required product")
                return redirect("sale")

            quantityproduct = int(product_id.qty) - int(qty)
            product_id.qty = quantityproduct

            harga = int(qty) * int(product_id.harga)

            product_id.save()

            sale.customer = customer
            sale.product = product_id
            sale.qty = qty
            sale.date_transaksi = date_transaksi
            sale.total_price = harga
            sale.save()

            messages.success(request, "berhasil update sale")

            return redirect("sale")
        else:
            messages.error(request, "Error pada input sale")
            return redirect("sale")


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
