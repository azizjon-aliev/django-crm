from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from src.apps.Common.models import TimeStampedModel, UserStampedModel


class CustomerRequest(TimeStampedModel, UserStampedModel):
	class RequestType(models.TextChoices):
		COMPLAINT = "complaint", _("Жалоба")
		SUGGESTION = "suggestion", _("Предложение")
		QUESTION = "question", _("Вопрос")
		TECHNICAL = "technical", _("Техническая проблема")
		BILLING = "billing", _("Проблема с оплатой")
		THANKS = "thanks", _("Благодарность")

	class ServiceType(models.TextChoices):
		MOBILE = "mobile", _("Мобильная связь")
		INTERNET = "internet", _("Интернет")
		TV = "tv", _("Телевидение")
		OTHER = "other", _("Другое")

	class Status(models.TextChoices):
		NEW = "new", _("Новое")
		IN_PROGRESS = "in_progress", _("В обработке")
		RESOLVED = "resolved", _("Решено")
		CLOSED = "closed", _("Закрыто")

	class PreferredContactMethod(models.TextChoices):
		PHONE = "phone", _("По телефону")
		EMAIL = "email", _("По электронной почте")
		MESSENGER = "messenger", _("Через мессенджер")

	first_name = models.CharField(
		max_length=100, verbose_name=_("Имя"), help_text=_("Введите имя клиента")
	)
	last_name = models.CharField(
		max_length=100,
		verbose_name=_("Фамилия"),
		help_text=_("Введите фамилию клиента"),
	)
	phone_number = models.CharField(
		max_length=20,
		verbose_name=_("Номер телефона"),
		help_text=_("Введите номер телефона клиента"),
		validators=[
			RegexValidator(
				regex=r'^\+992\d{9}$',
				message=_("Номер телефона должен начинаться с +992 и содержать 9 цифр после кода страны."),
			),
		],
	)
	email = models.EmailField(
		verbose_name=_("Электронная почта"),
		help_text=_("Введите электронную почту клиента"),
	)
	address = models.TextField(
		verbose_name=_("Адрес"),
		blank=True,
		null=True,
		help_text=_("Введите адрес клиента"),
	)
	request_type = models.CharField(
		max_length=20,
		choices=RequestType.choices,
		verbose_name=_("Тип обращения"),
		default=RequestType.QUESTION,
		help_text=_("Выберите тип обращения клиента"),
	)
	subject = models.CharField(
		max_length=200,
		verbose_name=_("Тема обращения"),
		help_text=_("Введите тему обращения"),
	)
	description = models.TextField(
		verbose_name=_("Описание проблемы"),
		help_text=_("Введите подробное описание проблемы"),
	)
	contract_number = models.CharField(
		max_length=50,
		verbose_name=_("Лицевой счет/договор"),
		blank=True,
		null=True,
		help_text=_("Введите номер лицевого счета или договора"),
	)
	service_phone_number = models.CharField(
		max_length=20,
		verbose_name=_("Номер телефона услуги"),
		blank=True,
		null=True,
		help_text=_("Введите номер телефона, связанный с услугой"),
		validators=[
			RegexValidator(
				regex=r'^\+992\d{9}$',
				message=_("Номер телефона должен начинаться с +992 и содержать 9 цифр после кода страны."),
			),
		],
	)

	service_type = models.CharField(
		max_length=50,
		choices=ServiceType.choices,
		verbose_name=_("Тип услуги"),
		blank=True,
		null=True,
		help_text=_("Выберите тип услуги"),
	)
	attachment = models.FileField(
		upload_to="attachments/",
		verbose_name=_("Прикрепленный файл"),
		blank=True,
		null=True,
		help_text=_("Прикрепите соответствующие файлы (например, скриншоты, чеки)"),
	)
	preferred_contact_method = models.CharField(
		max_length=50,
		choices=PreferredContactMethod.choices,
		verbose_name=_("Предпочтительный способ связи"),
		help_text=_("Выберите предпочтительный способ связи"),
	)
	incident_date = models.DateTimeField(
		verbose_name=_("Дата и время инцидента"),
		blank=True,
		null=True,
		help_text=_("Введите дату и время инцидента"),
	)
	status = models.CharField(
		max_length=50,
		choices=Status.choices,
		default=Status.NEW,
		verbose_name=_("Статус обращения"),
		help_text=_("Выберите текущий статус обращения"),
	)
	assigned_to = models.ForeignKey(
		User,
		on_delete=models.SET_NULL,
		verbose_name=_("Ответственное лицо"),
		blank=True,
		null=True,
		related_name="assigned_requests",
		help_text=_("Выберите пользователя, ответственного за обработку обращения"),
	)
	internal_comment = models.TextField(
		verbose_name=_("Комментарий сотрудника"),
		blank=True,
		null=True,
		help_text=_("Добавьте внутренний комментарий для сотрудников"),
	)

	def __str__(self):
		return f"{self.first_name} {self.last_name} - {self.subject}"

	class Meta:
		verbose_name = _("Обращение клиента")
		verbose_name_plural = _("Обращения клиентов")
		indexes = [
			models.Index(fields=["first_name"]),
			models.Index(fields=["last_name"]),
			models.Index(fields=["email"]),
			models.Index(fields=["phone_number"]),
			models.Index(fields=["subject"]),
			models.Index(fields=["contract_number"]),
		]
