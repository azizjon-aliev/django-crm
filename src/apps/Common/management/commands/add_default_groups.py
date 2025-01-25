from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from src.config import settings

User = get_user_model()


class Command(BaseCommand):
	help = "Create default groups and assign default permissions after migration."

	def handle(self, *args, **options):
		default_groups = {
			settings.OPERATOR_GROUP_NAME: [
				"view_customerrequest",
				"add_customerrequest",
				"change_customerrequest",
			],
			settings.BACK_OFFICE_GROUP_NAME: [
				"view_customerrequest",
				"change_customerrequest",
			],
		}

		for group_name, permissions in default_groups.items():
			group, created = Group.objects.get_or_create(name=group_name)
			if created:
				for perm in permissions:
					permission = Permission.objects.get(codename=perm)
					group.permissions.add(permission)

		self.stdout.write(
			self.style.SUCCESS("Default groups and permissions have been created.")
		)
