from django.contrib import admin
from .models import ServicesModel, WorkshopModel, EducationalBackgroundsModel, CityModel, UserModel

admin.site.register(ServicesModel)
admin.site.register(WorkshopModel)
admin.site.register(EducationalBackgroundsModel)
admin.site.register(CityModel)
admin.site.register(UserModel)
