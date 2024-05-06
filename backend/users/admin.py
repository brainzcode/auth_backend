from django.contrib import admin

from .models import UserAccount
# from import_export.admin import ImportExportModelAdmin


class UserAccountAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "email",
        "first_name",
        "last_name",
    ]
    list_filter = ["date_joined", "is_active"]


admin.site.register(UserAccount, UserAccountAdmin)
