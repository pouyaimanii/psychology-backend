from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager



class ServicesModel(models.Model):
    title = models.CharField(max_length=100)
    


class WorkshopModel(models.Model):
    title = models.CharField(max_length=100)


class EducationalBackgroundsModel(models.Model):
    title = models.CharField(max_length=100)


class CityModel(models.Model):
    name = models.CharField(max_length=120)
























class CustomUserManager(BaseUserManager):
    def create_user(self, name, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        user = self.model(name=name, **extra_fields)
        user.set_unusable_password()  # پسورد را غیرفعال می‌کند
        user.save(using=self._db)
        return user

    def create_superuser(self, name="ادمین", password=None, **extra_fields): #TODO role 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        user = self.model(name=name, **extra_fields)
        
        if password:
            user.set_password(password)  # پسورد را فعال می‌کند برای سوپر یوزر
        
        user.save(using=self._db)
       
        return user
        

    def get_by_natural_key(self, phone_number):
        return self.get(phone_number=phone_number)




class UserModel(AbstractBaseUser):
    CONSULTING_TIME_CHOICES = (
        ('ten', '10'),
        ('fifteen', '15'),
        ('twenty', '20'),
        ('twentyFive', '25'),
        ('thirty', '30'),
        ('thirtyFive', '35'),
        ('forty', '40'),
        ('fortyFive', '45'),
        ('fifty', '50'),
        ('fiftyFive', '55'),
        ('sixty', '60'),
    )
    
    name = models.CharField(max_length=150)
    lastName = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    nationalCode = models.CharField(max_length=22)
    age = models.CharField(max_length=3)
    image = models.ImageField(upload_to="userImage/", null=True, blank=True)
    descriptions = models.TextField()
    job = models.CharField(max_length=100, default="مشاور ، روانشناس")
    office_address = models.TextField(max_length=1000)
    phone_number_consulting = models.CharField(max_length=20)
    consulting_time = models.CharField(max_length=50, choices=CONSULTING_TIME_CHOICES, default="ten")
    status = models.BooleanField(default=False)

    services = models.ManyToManyField(ServicesModel)
    education = models.ManyToManyField(EducationalBackgroundsModel)
    workshops = models.ManyToManyField(WorkshopModel)
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'phone_number' 
  



    objects = CustomUserManager()




    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True  # منطق خودتان را اضافه کنید

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        return True  # منطق خودتان را اضافه کنید


    def __str__(self):
        return self.phone_number






