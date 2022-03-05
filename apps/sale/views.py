from django.shortcuts import render
from .models import Sale

# Create your views here.
def saleList(request):
    sale = Sale.objects.all()

    context = {
        "sale": Sale
    }

    return render(request, 'sale/index.html', context)

def saleCreate(request):
    if request.method == 'POST':
        name = request.POST['name']
        alamat = request.POST['alamat']
        email = request.POST['email']
        telepon = request.POST['telepon']

        Sale.objects.create(name=name,alamat=alamat,email=email,telepon=telepon)

        return redirect('sale')

    else:
        return render(request,'sale/create.html')
