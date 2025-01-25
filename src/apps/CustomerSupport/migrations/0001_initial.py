# Generated by Django 5.1.5 on 2025-01-25 08:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomerRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
                ),
                (
                    "first_name",
                    models.CharField(
                        help_text="Введите имя клиента",
                        max_length=100,
                        verbose_name="Имя",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        help_text="Введите фамилию клиента",
                        max_length=100,
                        verbose_name="Фамилия",
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        help_text="Введите номер телефона клиента",
                        max_length=20,
                        verbose_name="Номер телефона",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Введите электронную почту клиента",
                        max_length=254,
                        verbose_name="Электронная почта",
                    ),
                ),
                (
                    "address",
                    models.TextField(
                        blank=True,
                        help_text="Введите адрес клиента",
                        null=True,
                        verbose_name="Адрес",
                    ),
                ),
                (
                    "request_type",
                    models.CharField(
                        choices=[
                            ("complaint", "Жалоба"),
                            ("suggestion", "Предложение"),
                            ("question", "Вопрос"),
                            ("technical", "Техническая проблема"),
                            ("billing", "Проблема с оплатой"),
                            ("thanks", "Благодарность"),
                        ],
                        default="question",
                        help_text="Выберите тип обращения клиента",
                        max_length=20,
                        verbose_name="Тип обращения",
                    ),
                ),
                (
                    "subject",
                    models.CharField(
                        help_text="Введите тему обращения",
                        max_length=200,
                        verbose_name="Тема обращения",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите подробное описание проблемы",
                        verbose_name="Описание проблемы",
                    ),
                ),
                (
                    "contract_number",
                    models.CharField(
                        blank=True,
                        help_text="Введите номер договора, если применимо",
                        max_length=50,
                        null=True,
                        verbose_name="Номер договора",
                    ),
                ),
                (
                    "service_phone_number",
                    models.CharField(
                        blank=True,
                        help_text="Введите номер телефона, связанный с услугой",
                        max_length=20,
                        null=True,
                        verbose_name="Номер телефона услуги",
                    ),
                ),
                (
                    "service_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("mobile", "Мобильная связь"),
                            ("internet", "Интернет"),
                            ("tv", "Телевидение"),
                            ("other", "Другое"),
                        ],
                        help_text="Выберите тип услуги",
                        max_length=50,
                        null=True,
                        verbose_name="Тип услуги",
                    ),
                ),
                (
                    "attachment",
                    models.FileField(
                        blank=True,
                        help_text="Прикрепите соответствующие файлы (например, скриншоты, чеки)",
                        null=True,
                        upload_to="attachments/",
                        verbose_name="Прикрепленный файл",
                    ),
                ),
                (
                    "preferred_contact_method",
                    models.CharField(
                        choices=[
                            ("phone", "По телефону"),
                            ("email", "По электронной почте"),
                            ("messenger", "Через мессенджер"),
                        ],
                        help_text="Выберите предпочтительный способ связи",
                        max_length=50,
                        verbose_name="Предпочтительный способ связи",
                    ),
                ),
                (
                    "incident_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="Введите дату и время инцидента",
                        null=True,
                        verbose_name="Дата и время инцидента",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "Новое"),
                            ("in_progress", "В обработке"),
                            ("resolved", "Решено"),
                            ("closed", "Закрыто"),
                        ],
                        default="new",
                        help_text="Выберите текущий статус обращения",
                        max_length=50,
                        verbose_name="Статус обращения",
                    ),
                ),
                (
                    "internal_comment",
                    models.TextField(
                        blank=True,
                        help_text="Добавьте внутренний комментарий для сотрудников",
                        null=True,
                        verbose_name="Комментарий сотрудника",
                    ),
                ),
                (
                    "assigned_to",
                    models.ForeignKey(
                        blank=True,
                        help_text="Выберите пользователя, ответственного за обработку обращения",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="assigned_requests",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Ответственное лицо",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Создано пользователем",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_updated_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Обновлено пользователем",
                    ),
                ),
            ],
            options={
                "verbose_name": "Обращение клиента",
                "verbose_name_plural": "Обращения клиентов",
            },
        ),
    ]
