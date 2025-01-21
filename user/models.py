from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, name, phone_number, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone number must be set')
        user = self.model(name=name, phone_number=phone_number, **extra_fields)
        user.set_unusable_password()  # پسورد را غیرفعال می‌کند
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, name="ادمین", password=None, **extra_fields): #TODO role 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        user = self.model(name=name, phone_number=phone_number, **extra_fields)
        
        if password:
            user.set_password(password)  # پسورد را فعال می‌کند برای سوپر یوزر
        
        user.save(using=self._db)
       
        return user
        

    def get_by_natural_key(self, phone_number):
        return self.get(phone_number=phone_number)




class UserModel(AbstractBaseUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('simple', 'Simple User'),
        ('authenticated', 'Authenticated User')
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="simple")
    name = models.CharField(max_length=150)
    lastName = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    nationalCode = models.CharField(max_length=22)
    city = models
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'phone_number' 
    # REQUIRED_FIELDS = ['phone_number'] 



    objects = CustomUserManager()




    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True  # منطق خودتان را اضافه کنید

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        return True  # منطق خودتان را اضافه کنید


    def __str__(self):
        return self.phone_number






