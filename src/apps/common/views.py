from django.shortcuts import redirect
from django.urls import reverse


def redirect_to_admin(request):
    return redirect(reverse("customer_support:requests_list"))
