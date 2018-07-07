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
            reverse_action('create'),
            self.food_data,
            format="json")

    def test_api_can_create_a_food(self):
        """Test the api has food creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_food(self):
        """Test the api can get a given food."""
        food = Food.objects.get()
        response = self.client.get(
          reverse('details', kwargs={'pk': food.id}),
          format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, food)

    def test_api_can_update_food(self):
        """Test the api can update a given food."""
        food = Food.objects.get()
        change_food = {'name': 'Something new', 'calories': '100'}
        res = self.client.put(
          reverse('details', kwargs={'pk': food.id}),
          change_food, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_food(self):
        """Test the api can delete a food."""
        food = Food.objects.get()
        response = self.client.delete(
          reverse('details', kwargs={'pk': food.id}),
          format='json',
          follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
