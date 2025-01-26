from django.urls import path
from src.apps.users.views import custom_logout, LoginUserView

app_name = "users"

urlpatterns = [
    path("login/", LoginUserView.as_view(), name="login"),
    path("logout/", custom_logout, name="logout"),
]
