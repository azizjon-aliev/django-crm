from django.contrib import admin

from src.config import settings
from .models import CustomerRequest


@admin.register(CustomerRequest)
class CustomerRequestAdmin(admin.ModelAdmin):
	list_display = (
		"first_name",
		"last_name",
		"subject",
		"request_type",
		"status",
		"assigned_to",
		"incident_date",
	)
	list_filter = ("request_type", "status", "service_type", "preferred_contact_method")
	search_fields = (
		"first_name",
		"last_name",
		"email",
		"phone_number",
		"subject",
		"description",
		"contract_number",
	)
	autocomplete_fields = ("assigned_to",)

	fieldsets = (
		(
			None,
			{"fields": ("first_name", "last_name", "phone_number", "email", "address")},
		),
		(
			"Детали обращения",
			{
				"fields": (
					"request_type",
					"subject",
					"description",
					"contract_number",
					"service_phone_number",
					"service_type",
					"attachment",
					"preferred_contact_method",
					"incident_date",
				)
			},
		),
		(
			"Статус и назначение",
			{"fields": ("status", "assigned_to", "internal_comment")},
		),
		("Временные метки", {"fields": ("created_at", "updated_at")}),
		("Создано/изменено", {"fields": ("created_by", "updated_by")}),
	)

	def get_readonly_fields(self, request, obj=...):
		readonly_fields = ["created_at", "updated_at", "created_by", "updated_by"]

		if request.user.groups.filter(name=settings.OPERATOR_GROUP_NAME).exists():
			readonly_fields += ["status", "internal_comment"]

		elif request.user.groups.filter(name=settings.BACK_OFFICE_GROUP_NAME).exists():
			readonly_fields += [
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
			]

		return readonly_fields

	def save_model(self, request, obj, form, change):
		if not obj.pk:
			obj.created_by = request.user
		obj.updated_by = request.user
		super().save_model(request, obj, form, change)
