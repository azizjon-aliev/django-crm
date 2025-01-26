from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class TimeStampedModel(models.Model):
    """Abstract base class with created and updated timestamps."""

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    class Meta:
        abstract = True


class UserStampedModel(models.Model):
    """Abstract base class with created_by and updated_by user references."""

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_created_by",
        verbose_name=_("Создано пользователем"),
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_updated_by",
        verbose_name=_("Обновлено пользователем"),
    )

    class Meta:
        abstract = True
