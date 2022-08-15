from django.contrib import admin
from  .models import  User

class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "nick_name", "balance")
    readonly_fields = ("email", "nick_name", "balance", "is_superuser", "is_staff", "is_active",
                            "groups", "user_permissions", "last_login", "password")

admin.site.register(User, UserAdmin)