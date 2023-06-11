from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Work_Permit, Payment, ContactMessage, Recruiters_License_and_Permits, Residence_Permit


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('email', 'date','email', 'name', 'surname', 'message')
    search_fields = ('email','date',)
    list_filter = ('date',)
    ordering = ('date',)

class WorkPermitAdmin(admin.ModelAdmin):
    list_display = ('user', 'date','amount','service','reason_for_application', 'marital_status', 'passport_number', 'passport_number_expiry_date','approval_status','payment_status','cv_pdf','certified_copy_of_passport_pdf','certified_copy_of_certificates_pdf')
    search_fields = ('date','passport_number','approval_status','payment_status')
    list_filter = ('marital_status','passport_number','approval_status',)
    ordering = ('date',)

class ResidencePermitAdmin(admin.ModelAdmin):
    list_display = ('user', 'date','amount','service', 'reason_for_application', 'marital_status', 'passport_number', 'passport_number_expiry_date','approval_status','payment_status','cv_pdf','certified_copy_of_passport_pdf','certified_copy_of_certificates_pdf')
    search_fields = ('date','passport_number','approval_status','payment_status')
    list_filter = ('marital_status','passport_number','approval_status',)
    ordering = ('date',)


class Recruiters_License_and_PermitsAdmin(admin.ModelAdmin):
    list_display = ('user', 'date','amount','service', 'reason_for_application','approval_status','payment_status')
    search_fields = ('date','approval_status','payment_status')
    list_filter = ('payment_status','approval_status',)
    ordering = ('date',)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date','approval_status','payment_status','amount','service')
    search_fields = ('date', 'approval_status','payment_status',)
    list_filter = ('approval_status','payment_status',)
    ordering = ('date',)

admin.site.register(ContactMessage, ContactFormAdmin)
admin.site.register(Work_Permit, WorkPermitAdmin)
admin.site.register(Residence_Permit, ResidencePermitAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Recruiters_License_and_Permits, Recruiters_License_and_PermitsAdmin)
