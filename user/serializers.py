from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['name', 'lastName', 'phone_number', 'nationalCode', 'age', 'image', 
                  'descriptions', 'job', 'office_address', 'phone_number_consulting', 
                  'consulting_time', 'services', 'education', 'workshops', 'city', 
                  'is_verified', 'is_active', 'status']
        extra_kwargs = {
            'phone_number': {'required': True},
            'name': {'required': True}
        }

    def create(self, validated_data):
        services_data = validated_data.pop('services', [])  # حذف داده‌های many-to-many
        education_data = validated_data.pop('education', [])
        workshops_data = validated_data.pop('workshops', [])
        user = UserModel.objects.create_user(**validated_data)

        # مقداردهی به فیلدهای ManyToMany بعد از ایجاد کاربر
        user.services.set(services_data)
        user.education.set(education_data)
        user.workshops.set(workshops_data)
        
        return user


        # user = UserModel.objects.create_user(**validated_data)
        # return user


