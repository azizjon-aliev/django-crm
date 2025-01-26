from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import DeleteView, DetailView, CreateView, UpdateView
from django_filters.views import FilterView

from .filters import CustomerRequestFilter
from .forms import CustomerEditRequestForm, CustomerRequestForm
from src.apps.CustomerSupport.models import CustomerRequest


class BaseRequestView(LoginRequiredMixin):
    model = CustomerRequest
    login_url = reverse_lazy("users:login")
    redirect_field_name = "next"


class RequestEditView(BaseRequestView, UpdateView):
    model = CustomerRequest
    form_class = CustomerEditRequestForm
    template_name = "CustomerSupport/requests_edit.html"
    success_url = reverse_lazy("customer_support:requests_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Изменить обращение"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _("Обращение успешно изменено!"))
        return response


class RequestDeleteView(BaseRequestView, DeleteView):
    model = CustomerRequest
    success_url = reverse_lazy("customer_support:requests_list")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _("Обращение успешно удалено."))
        return super().delete(request, *args, **kwargs)


class RequestListView(BaseRequestView, FilterView):
    template_name = "CustomerSupport/requests_list.html"
    context_object_name = "requests"
    paginate_by = 5
    filterset_class = CustomerRequestFilter

    def get_queryset(self):
        queryset = super().get_queryset()

        # Поиск по запросу
        search_query = self.request.GET.get("search")
        if search_query:
            queryset = queryset.filter(
                models.Q(first_name__icontains=search_query)
                | models.Q(last_name__icontains=search_query)
                | models.Q(phone_number__icontains=search_query)
                | models.Q(email__icontains=search_query)
                | models.Q(subject__icontains=search_query)
            )

        # Сортировка по умолчанию (новые вверху)
        sort_by = self.request.GET.get("sort_by", "-created_at")
        if sort_by.lstrip("-") in [  # Убираем минус для проверки
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "subject",
            "status",
            "created_at",
        ]:
            queryset = queryset.order_by(sort_by)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("search", "")
        context["sort_by"] = self.request.GET.get("sort_by", "-created_at")
        return context


class RequestDetailView(BaseRequestView, DetailView):
    template_name = "CustomerSupport/requests_detail.html"
    context_object_name = "request"


class RequestCreateView(CreateView, BaseRequestView):
    form_class = CustomerRequestForm
    template_name = "CustomerSupport/requests_create.html"
    success_url = reverse_lazy("customer_support:requests_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Добавить обращение")
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _("Обращение успешно создано!"))
        return response
