import django_filters
from .models import CustomerRequest
from django.utils.translation import gettext_lazy as _


class CustomerRequestFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(
        choices=CustomerRequest.Status.choices, label=_("Статус")
    )
    request_type = django_filters.ChoiceFilter(
        choices=CustomerRequest.RequestType.choices, label=_("Тип обращения")
    )
    service_type = django_filters.ChoiceFilter(
        choices=CustomerRequest.ServiceType.choices, label=_("Тип услуги")
    )

    class Meta:
        model = CustomerRequest
        fields = ["status", "request_type", "service_type"]
