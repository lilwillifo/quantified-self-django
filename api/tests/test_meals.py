from django.test import TestCase
from api.models import Food
from api.models import Meal
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from api.views import FoodViews
class MealViewsTest(TestCase):
    """Test suite for the meal api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.apple = Food.objects.create(name="apple", calories=50)
        self.oatmeal = Food.objects.create(name="oatmeal", calories=400)
        self.breakfast = Meal.objects.create(name="breakfast")
        self.snack = Meal.objects.create(name="snack")
        self.lunch = Meal.objects.create(name="lunch")
        self.dinner = Meal.objects.create(name="dinner")
        self.breakfast.foods.add(self.apple)

    def test_gets_all_meals(self):
        response = self.client.get('/api/v1/meals/')
        js = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(js), 4)
        self.assertEqual(js[0]["name"], self.breakfast.name)
        self.assertEqual(js[1]["name"], self.snack.name)
        self.assertEqual(js[2]["name"], self.lunch.name)
        self.assertEqual(js[3]["name"], self.dinner.name)

    def test_gets_single_meal(self):
        meal_id = str(self.breakfast.id)
        response = self.client.get(f'/api/v1/meals/{meal_id}/foods')

        meal_response = response.json()

        self.assertEqual(meal_response['name'], 'Breakfast')
        self.assertEqual(meal_response['foods'][0]['name'], self.apple.name)
        self.assertEqual(meal_response['foods'][0]['calories'], self.apple.calories)
