from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse


def custom_logout(request):
    logout(request)
    return redirect(reverse("customer_support:requests_list"))


class LoginUserView(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True
