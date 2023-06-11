from django.urls import path
from .import views

urlpatterns = [
    path('', views.lss_home, name='lss_home'),
    path('emc/', views.emc_home, name='emc_home'),
    path('contact_view/', views.contact_view, name='contact_view'),
    path('faq/', views.faq, name='faq'),
    path('work_permit/', views.work_permit, name='work_permit'),
    path('residence_permit/', views.residence_permit, name='residence_permit'),
    path('recruiters/', views.recruiters, name='recruiters'),
    path('my_applications/', views.my_applications, name='my_applications'),
    path('my_payments/', views.my_payments, name='my_payments'),
    path('update_payment_status/', views.update_payment_status, name='update_payment_status'),
]