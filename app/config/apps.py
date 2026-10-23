from django.contrib.admin.apps import AdminConfig


class StaffAdminConfig(AdminConfig):
    default_site = "config.admin.StaffAdminSite"
