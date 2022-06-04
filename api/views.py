from rest_framework import viewsets
from django.shortcuts import render

from .models import Meal, Rating
from .serializers import MealSerailizer, RatingSerializer

# Create your views here.

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerailizer




class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
