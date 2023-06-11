from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'id_number',)
    search_fields = ('email', 'id_number',)
    list_filter = ('gender',)
    ordering = ('gender',)

admin.site.register(Account, AccountAdmin)
