from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Work_Permit)
def create_basket_from_work_permit(sender, instance, created, **kwargs):
    if created:
        Payment.objects.create(
            user=instance.user,
            date=instance.date,
            service=instance.service,
            approval_status=instance.payment_status,
            payment_status=instance.payment_status,
            amount=instance.amount
        )


@receiver(post_save, sender=Residence_Permit)
def create_basket_from_residence_permit(sender, instance, created, **kwargs):
    if created:
        Payment.objects.create(
            user=instance.user,
            date=instance.date,
            service=instance.service,
            approval_status=instance.payment_status,
            payment_status=instance.payment_status,
            amount=instance.amount
        )


@receiver(post_save, sender=Recruiters_License_and_Permits)
def create_basket_from_Recruiters_License_and_Permits(sender, instance, created, **kwargs):
    if created:
        Payment.objects.create(
            user=instance.user,
            date=instance.date,
            service=instance.service,
            approval_status=instance.payment_status,
            payment_status=instance.payment_status,
            amount=instance.amount
        )