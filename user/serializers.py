from rest_framework import serializers
from .models import UserModel, ServicesModel, WorkshopModel, EducationalBackgroundsModel, CityModel
 
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = ['id' ,'name']


class EducationalBackgroundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalBackgroundsModel
        fields = ['id' ,'title']




class UserSerializer(serializers.ModelSerializer):
    education = EducationalBackgroundsSerializer(many=True, read_only=True)
    city = CitySerializer(read_only=True)
    city_id = serializers.PrimaryKeyRelatedField(
        queryset=CityModel.objects.all(), source='city', write_only=True
    ) 

    class Meta:
        model = UserModel
        fields = ['id','name', 'lastName', 'phone_number', 'nationalCode', 'age', 'image', 
                  'descriptions', 'job', 'office_address', 'phone_number_consulting', 
                  'consulting_time', 'services', 'education', 'workshops', 'city', 'city_id', 
                  'is_verified', 'is_active', 'status', 'telegram', 'instagram', 'education_image', 'rank', 'system_code',]
        extra_kwargs = {
            'phone_number': {'required': True},
            'name': {'required': True}
        }

    def create(self, validated_data):
        services_data = validated_data.pop('services', [])  
        education_data = validated_data.pop('education', [])
        workshops_data = validated_data.pop('workshops', [])
        user = UserModel.objects.create_user(**validated_data)

        user.services.set(services_data)
        user.education.set(education_data)
        user.workshops.set(workshops_data)
        
        return user
    




class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesModel
        fields = ['id', 'title']


class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopModel
        fields = ['id' ,'title']

