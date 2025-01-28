from django import forms
from .models import CustomerRequest
from django.utils.translation import gettext_lazy as _


class NonValidatingChoiceField(forms.ChoiceField):
	def valid_value(self, value):
		return True

	def clean(self, value):
		return value


class CustomerRequestAdminForm(forms.ModelForm):
	class Meta:
		model = CustomerRequest
		fields = '__all__'
		widgets = {
			'phone_number': forms.TextInput(attrs={'placeholder': '+992XXXXXXXXX'}),
			'service_phone_number': forms.TextInput(attrs={'placeholder': '+992XXXXXXXXX'}),
		}


class CustomerEditRequestForm(forms.ModelForm):
	subject = NonValidatingChoiceField(choices=[])

	class Meta:
		model = CustomerRequest
		fields = '__all__'
		widgets = {
			'request_type': forms.Select(attrs={'onchange': 'updateSubjects()'}),
			"description": forms.Textarea(attrs={"rows": 4}),
			"internal_comment": forms.Textarea(attrs={"rows": 4}),
			"incident_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# Инициализируем варианты для subject
		if self.instance and self.instance.pk:
			self.fields['subject'].choices = self.instance.SUBJECT_CHOICES.get(
				self.instance.request_type, []
			)
		else:
			self.fields['subject'].choices = []

	def clean_subject(self):
		return self.cleaned_data.get('subject')

	def clean(self):
		cleaned_data = super().clean()
		request_type = cleaned_data.get('request_type')
		subject = cleaned_data.get('subject')

		# Валидация соответствия темы и типа обращения
		valid_subjects = dict(self.instance.SUBJECT_CHOICES.get(request_type, []))
		if subject not in valid_subjects:
			self.add_error(
				'subject',
				_('Недопустимая тема для выбранного типа обращения')
			)

		return cleaned_data


class CustomerRequestForm(forms.ModelForm):
	class Meta:
		model = CustomerRequest
		fields = [
			"first_name",
			"last_name",
			"phone_number",
			"email",
			"address",
			"request_type",
			"subject",
			"description",
			"contract_number",
			"service_phone_number",
			"service_type",
			"attachment",
			"preferred_contact_method",
			"incident_date",
			"status",
			"assigned_to",
			"internal_comment",
		]
		widgets = {
			"incident_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
			"description": forms.Textarea(attrs={"rows": 3}),
			"internal_comment": forms.Textarea(attrs={"rows": 3}),
		}
		labels = {
			"first_name": _("Имя"),
			"last_name": _("Фамилия"),
			"phone_number": _("Номер телефона"),
			"email": _("Электронная почта"),
			"address": _("Адрес"),
			"request_type": _("Тип обращения"),
			"subject": _("Тема"),
			"description": _("Описание проблемы"),
			"contract_number": _("Лицевой счет/договор"),
			"service_phone_number": _("Номер телефона услуги"),
			"service_type": _("Тип услуги"),
			"attachment": _("Прикрепленный файл"),
			"preferred_contact_method": _("Предпочтительный способ связи"),
			"incident_date": _("Дата и время инцидента"),
			"status": _("Статус"),
			"assigned_to": _("Ответственное лицо"),
			"internal_comment": _("Комментарий сотрудника"),
		}
