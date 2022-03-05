from django.shortcuts import render, redirect
from .models import Customer

# Create your views here.

def customerList(request):
    customer = Customer.objects.all()

    context = {
        "customer": customer
    }

    return render(request,'customer/index.html', context)
    

def customerCreate(request):
    if request.method == "POST":
        name = request.POST['name']
        alamat = request.POST['alamat']
        email = request.POST['email']
        telepon = request.POST['telepon']

        Customer.objects.create(name=name,alamat=alamat,email=email,telepon=telepon)

        return redirect('customer')
    else:
        return render(request, 'customer/create.html')
        

def customerUpdate(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['name']
        alamat = request.POST['alamat']
        email = request.POST['email']
        telepon = request.POST['telepon']

        customer.name = name
        customer.alamat = alamat
        customer.email = email
        customer.telepon = telepon

        customer.save();

        return rediret('customer')
    else:
        return render(request, 'customer/update.html')

def customerDelete(request, id):
    customer = Customer.objects.get(id=id)

    try:
        customer.delete()

        return redirect('customer')
    except Customer.DoesNotExist:
        raise Exception("Ga bisa");
