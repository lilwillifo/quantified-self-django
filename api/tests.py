from django.test import TestCase
from .models import Food
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ModelTestCase(TestCase):
    """This class defines the test suite for the food model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.food_name = "Banana"
        self.food_calories = 50
        self.food = Food(name=self.food_name, calories=self.food_calories)

    def test_model_can_create_a_food(self):
        """Test the food model can create a food."""
        old_count = Food.objects.count()
        self.food.save()
        new_count = Food.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.food_data = {'name': 'Oatmeal', 'calories': '500'}
        self.response = self.client.post(
            reverse('create'),
            self.food_data,
            format="json")

    def test_api_can_create_a_food(self):
        """Test the api has food creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
