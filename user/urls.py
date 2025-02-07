from django.contrib import admin
from django.urls import path, include
from .views import UserCreateView, EducationalBackgroundsView, CityView, ServiceView, WorkshopView, PsychologistsView
urlpatterns = [
    path('singup/', UserCreateView.as_view(), name="singup"),
    path('services/', ServiceView.as_view(), name="services"),
    path('workshops/', WorkshopView.as_view(), name="workshops"),
    path('cities/', CityView.as_view(), name="cities"),
    path('educationalBackgrounds/', EducationalBackgroundsView.as_view(), name="educationalbzackgrounds"),
    path('psychologists/', PsychologistsView.as_view(), name="psychologists")
]