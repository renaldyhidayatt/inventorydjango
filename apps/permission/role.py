from django.shortcuts import redirect


def authenticated_User(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_superuser:
            return redirect("home")
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func
