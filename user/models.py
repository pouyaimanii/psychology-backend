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
        user.set_unusable_password()  
        user.save(using=self._db)
        return user

    def create_superuser(self, name="ادمین", password=None, **extra_fields): #TODO role 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        user = self.model(name=name, **extra_fields)
        
        if password:
            user.set_password(password) 
        
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
    nationalCode = models.CharField(max_length=22, null=True, blank=True)
    age = models.CharField(max_length=3, null=True, blank=True)
    image = models.ImageField(upload_to="userImage/", null=True, blank=True)
    descriptions = models.TextField(null=True, blank=True)
    job = models.CharField(max_length=100, default="مشاور ، روانشناس")
    office_address = models.TextField(max_length=1000, null=True, blank=True)
    phone_number_consulting = models.CharField(max_length=20, null=True, blank=True)
    consulting_time = models.CharField(max_length=50, choices=CONSULTING_TIME_CHOICES, default="ten", null=True, blank=True)
    status = models.BooleanField(default=False)
    telegram = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    education_image = models.ImageField(upload_to="userImage/", null=True, blank=True)
    rank = models.BooleanField(default=False)
    system_code = models.CharField(max_length=100, null=True, blank=True)
    
    services = models.ManyToManyField(ServicesModel, null=True, blank=True)
    education = models.ManyToManyField(EducationalBackgroundsModel, null=True, blank=True)
    workshops = models.ManyToManyField(WorkshopModel, null=True, blank=True)
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'phone_number' 
  



    objects = CustomUserManager()




    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True 

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        return True  


    def __str__(self):
        return self.phone_number






