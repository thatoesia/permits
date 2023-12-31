# Generated by Django 4.2.1 on 2023-06-11 11:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('labour_and_social_security', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'Payment', 'verbose_name_plural': 'Payments'},
        ),
        migrations.AlterModelOptions(
            name='work_permit',
            options={'verbose_name': 'Work Permit', 'verbose_name_plural': 'Work Permits'},
        ),
        migrations.AlterField(
            model_name='work_permit',
            name='passport_number_expiry_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='work_permit',
            name='reason_for_application',
            field=models.CharField(help_text='type in less than 200 character', max_length=200),
        ),
    ]
