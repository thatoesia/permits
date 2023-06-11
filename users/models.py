from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, phone_number, date_of_birth, gender,
                    id_number, user_type, **other_fields):
        if not email:
            raise ValueError('you must provide an email')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name,
                          phone_number=phone_number, date_of_birth=date_of_birth, gender=gender, id_number=id_number, 
                          user_type=user_type, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, phone_number, date_of_birth, gender,
                         id_number, **other_fields):
        user = self.create_user(email=self.normalize_email(email), first_name=first_name,
                                last_name=last_name, password=password, phone_number=phone_number,
                                date_of_birth=date_of_birth, gender=gender, id_number=id_number, **other_fields)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    user_type_choices = (
        ('Citizen', 'Citizen'),
        ('Immigrant ', 'Immigrant '),
    )
    gender_choice = (
        ('Male','Male'),
        ('Female','Female'),
    )
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id_number = models.CharField(max_length=30)
    image = models.ImageField(upload_to='profile_images', blank=True, default='default_profile_pic.png')
    phone_number = models.CharField(max_length=30)
    gender = models.CharField(max_length=20, choices=gender_choice)
    date_of_birth = models.DateField(default=timezone.now)
    user_type = models.CharField(max_length=20, choices=user_type_choices)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'user_type','id_number', 'phone_number','gender','date_of_birth','image']

    objects = CustomAccountManager()

    def __str__(self):
        return self.email
