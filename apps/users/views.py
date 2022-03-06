from django.shortcuts import redirect, render
from .models import Users
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = auth.authenticate(email=email, password=password)

        auth.login(request, user)

        return redirect("home")
    else:
        return render(request, "auth/login.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        email = request.POST["email"]
        phone_number = request.POST["phone_number"]
        password = request.POST["password"]

        user = Users.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )

        user.phone_number = phone_number

        user.save()

        return redirect("login")

    else:
        return render(request, "auth/register.html")


def createuser(request):
    pass


def updateuser(request):
    pass


def deleteuser(request):
    pass
