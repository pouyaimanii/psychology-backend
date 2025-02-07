from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserModel, ServicesModel, CityModel, EducationalBackgroundsModel, WorkshopModel
from .serializers import UserSerializer, ServiceSerializer, EducationalBackgroundsSerializer, CitySerializer, WorkshopSerializer

class UserCreateView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ServiceView(APIView):
    def get(self, request):
        try:
            services = ServicesModel.objects.all()
        except:
            return Response({'error' : "services not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CityView(APIView):
    def get(self, request):
        try:
                cities = CityModel.objects.all()
        except:
            return Response({'error' : "services not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class WorkshopView(APIView):
    def get(self, request):
        try:
            workshops = WorkshopModel.objects.all()
        except:
            return Response({'error' : "services not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = WorkshopSerializer(workshops, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EducationalBackgroundsView(APIView):
    def get(self, request):
        try:
            records = EducationalBackgroundsModel.objects.all()
        except:
            return Response({'error' : "services not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = EducationalBackgroundsSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class PsychologistsView(APIView):
    def get(self, request):
        try:
            users = UserModel.objects.filter(status=True)
        except:
            return Response({"error" : "users not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    