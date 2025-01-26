from django.urls import path

from src.apps.CustomerSupport.views import (
    RequestDeleteView,
    RequestEditView,
    RequestListView,
    RequestDetailView,
    RequestCreateView,
)

app_name = "customer_support"

urlpatterns = [
    path("requests/create/", RequestCreateView.as_view(), name="requests_create"),
    path("requests/", RequestListView.as_view(), name="requests_list"),
    path("requests/<int:pk>/", RequestDetailView.as_view(), name="requests_detail"),
    path(
        "requests/<int:pk>/delete", RequestDeleteView.as_view(), name="requests_delete"
    ),
    path("requests/<int:pk>/edit", RequestEditView.as_view(), name="requests_edit"),
]
