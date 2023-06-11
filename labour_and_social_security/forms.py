from django import forms
from django.forms import ModelForm
from .models import Work_Permit, ContactMessage, Recruiters_License_and_Permits, Residence_Permit


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('email', 'name', 'surname', 'message')


class WorkPermitForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['amount'] = Work_Permit._meta.get_field('amount').get_default()

    class Meta:
        model = Work_Permit
        fields = ('service','reason_for_application','marital_status','nationality','passport_number','passport_number_expiry_date', 'cv_pdf','certified_copy_of_passport_pdf','certified_copy_of_certificates_pdf','amount')
        widgets = {
                    'amount': forms.TextInput(attrs={'readonly': 'readonly'}),
                    'passport_number_expiry_date':forms.DateInput(attrs={ "type": "date"})
        }

class ResidencePermitForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['amount'] = Residence_Permit._meta.get_field('amount').get_default()

    class Meta:
        model = Residence_Permit
        fields = ('service','reason_for_application','work_permit_no','number_of_children','marital_status','nationality','passport_number','passport_number_expiry_date', 
                  'cv_pdf','certified_copy_of_passport_pdf','certified_copy_of_certificates_pdf','amount')
        widgets = {
                    'amount': forms.TextInput(attrs={'readonly': 'readonly'}),
                    'passport_number_expiry_date':forms.DateInput(attrs={ "type": "date"})
                }



class RecruitersLicensePermitsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['amount'] = Recruiters_License_and_Permits._meta.get_field('amount').get_default()

    class Meta:
        model = Recruiters_License_and_Permits
        fields = ('service','reason_for_application','company_name','company_address','company_telephone','ids','cv_pdf',
                  'company_registration_doc','tax_clearance','compensation','bank_statement','lease_agreement','amount')
        widgets = {
                    'amount': forms.TextInput(attrs={'readonly': 'readonly'}),
                }