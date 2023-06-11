from django.apps import AppConfig


class LabourAndSocialSecurityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'labour_and_social_security'
    verbose_name = 'Work and Residence Permit System'

    def ready(self):
        import labour_and_social_security.signals