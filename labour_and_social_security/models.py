from django.db import models
from django.utils import timezone
from django.conf import settings


class ContactMessage(models.Model):
    date = models.DateField(default=timezone.now)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    message = models.TextField()

def __str__(self):
        return self.email


class Payment(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        service = models.CharField(max_length=300)
        date = models.DateField(default=timezone.now)
        approval_status = models.BooleanField(default=False)
        payment_status = models.BooleanField(default=False)
        amount = models.DecimalField(max_digits=10, decimal_places=2, default=200.00)

        class Meta: 
                verbose_name = "Payment"
                verbose_name_plural = "Payments"

class Work_Permit(models.Model):
    marital_status_choice = (
            ('Single', 'Single'),
            ('Divorced', 'Divorced'),
            ('Widower', 'Widower'),
            ('Other', 'Other'),
    )
    permit_choice = (
            ('Application of Work Permit', 'Application of Work Permit'),
            ('Renewal of Work Permit', 'Renewal of Work Permit'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service = models.CharField(max_length=200, choices=permit_choice)
    date = models.DateField(default=timezone.now)
    reason_for_application = models.CharField(max_length=200, help_text='type in less than 200 characters')
    marital_status = models.CharField(max_length=200, choices=marital_status_choice)
    nationality = models.CharField(max_length=200)
    passport_number = models.CharField(max_length=200)
    passport_number_expiry_date = models.DateField(default=timezone.now)
    approval_status = models.BooleanField(default=False)
    payment_status = models.BooleanField(default=False)
    cv_pdf = models.FileField(upload_to='cvs/')
    certified_copy_of_passport_pdf = models.FileField(upload_to='ids_and_passports/')
    certified_copy_of_certificates_pdf = models.FileField(upload_to='certificates/')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=250,help_text='BOTSWANA CURRENCY - BWP')
    
    class Meta:
        verbose_name = "Work Permit"
        verbose_name_plural = "Work Permits"


class Recruiters_License_and_Permits(models.Model):
        permit_choice = (
                ('Application of Recruiter License', 'Application of Recruiter License'),
                ('Renewal of Recruiter License', 'Renewal of Recruiter License'),
                )
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        service = models.CharField(max_length=200, choices=permit_choice)
        date = models.DateField(default=timezone.now)
        reason_for_application = models.CharField(max_length=200, help_text='type in less than 200 characters')
        company_name = models.CharField(max_length=200)
        company_address = models.CharField(max_length=200)
        company_telephone = models.CharField(max_length=200)
        cv_pdf = models.FileField(verbose_name='CVs of potential Recruiter’s permit holders',help_text='file must be in single pdf file',upload_to='certificates/')
        company_registration_doc = models.FileField(verbose_name='Company Registration Documents',help_text='file must be in pdf',upload_to='certificates/')
        lease_agreement = models.FileField(verbose_name='Lease Agreement',help_text='file must be in pdf',upload_to='certificates/')
        tax_clearance = models.FileField(verbose_name='Tax Clearance',help_text='file must be in pdf',upload_to='certificates/')
        compensation = models.FileField(verbose_name='Copy of Workers Compensation Insurance Certificate',help_text='file must be in pdf',upload_to='certificates/')
        bank_statement = models.FileField(verbose_name='Three (3) months Bank Statement',help_text='file must be in pdf',upload_to='certificates/')
        ids = models.FileField(verbose_name='Certified Identity Cards/ Work permits for Directors',help_text='file must be in a single pdf file',upload_to='ids_and_passports/')
        approval_status = models.BooleanField(default=False)
        payment_status = models.BooleanField(default=False)
        amount = models.DecimalField(max_digits=10, decimal_places=2, default=10000,help_text='BOTSWANA CURRENCY - BWP')
        
        class Meta:
                verbose_name = "Recruiters License and Permit"
                verbose_name_plural = "Recruiters License and Permits"


class Residence_Permit(models.Model):
    marital_status_choice = (
            ('Single', 'Single'),
            ('Divorced', 'Divorced'),
            ('Widower', 'Widower'),
            ('Other', 'Other'),
    )
    permit_choice = (
            ('Application of Residence Permit', 'Application of Residence Permit'),
            ('Renewal of Residence Permit', 'Renewal of Residence Permit'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service = models.CharField(max_length=200, choices=permit_choice)
    date = models.DateField(default=timezone.now)
    reason_for_application = models.CharField(max_length=200, help_text='type in less than 200 characters')
    marital_status = models.CharField(max_length=200, choices=marital_status_choice)
    nationality = models.CharField(max_length=200)
    work_permit_no = models.CharField(max_length=200)
    number_of_children = models.IntegerField()
    passport_number = models.CharField(max_length=200)
    passport_number_expiry_date = models.DateField(default=timezone.now)
    approval_status = models.BooleanField(default=False)
    payment_status = models.BooleanField(default=False)
    cv_pdf = models.FileField(upload_to='cvs/')
    certified_copy_of_passport_pdf = models.FileField(upload_to='ids_and_passports/')
    certified_copy_of_certificates_pdf = models.FileField(upload_to='certificates/')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=250,help_text='BOTSWANA CURRENCY - BWP')
    
    class Meta:
        verbose_name = "Residence Permit"
        verbose_name_plural = "Residence Permits"