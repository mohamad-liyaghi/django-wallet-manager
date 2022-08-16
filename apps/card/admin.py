from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "amount", "action")
    readonly_fields = ("title", "description", "action", "amount", "owner", "token")