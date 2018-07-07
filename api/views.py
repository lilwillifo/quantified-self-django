from rest_framework import generics
from .serializers import FoodSerializer
from .models import Food
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
import json

class FoodViews(viewsets.ViewSet):
    def list(self, request):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)

    def create(self, request):
        food_attrs = json.loads(request.body)['food']
        food = Food(name=food_attrs['name'], calories=food_attrs['calories'])
        food.save()
        serializer = FoodSerializer(food)
        return Response(serializer.data)
