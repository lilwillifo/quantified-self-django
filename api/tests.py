from django.test import TestCase
from .models import Food
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from .views import FoodViews

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

class FoodViewsTest(TestCase):
    """Test suite for the food api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.apple = Food.objects.create(name="apple", calories=50)
        self.oatmeal = Food.objects.create(name="oatmeal", calories=400)

    def test_status_for_all_foods(self):
        response = self.client.get('/api/v1/foods/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_gets_all_foods(self):
        response = self.client.get('/api/v1/foods/')
        js = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(js), 2)
        self.assertEqual(js[0]["name"], self.apple.name)
        self.assertEqual(js[0]["calories"], self.apple.calories)
        self.assertEqual(js[1]["name"], self.oatmeal.name)
        self.assertEqual(js[1]["calories"], self.oatmeal.calories)

    def test_api_can_create_a_food(self):
        """Test the api has food creation capability."""
        response = self.client.post('/api/v1/foods/', {'food': {'name': 'look at me a new food', 'calories': 2}}, format='json')
        # import code; code.interact(local=dict(globals(), **locals()))
        js = response.json()

        self.assertEqual(js["name"], "look at me a new food")
        self.assertEqual(js["calories"], 2)

    def test_api_can_get_a_food(self):
        """Test the api can get a given food."""
        food = Food.objects.first()

        response = self.client.get(f'/api/v1/foods/{food.id}')
        js = response.json()

        self.assertEqual(js["name"], self.apple.name)
        self.assertEqual(js["calories"], self.apple.calories)

    # def test_api_can_update_food(self):
    #     """Test the api can update a given food."""
    #     food = Food.objects.get()
    #     change_food = {'name': 'Something new', 'calories': '100'}
    #     res = self.client.put(
    #       reverse('details', kwargs={'pk': food.id}),
    #       change_food, format='json'
    #     )
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #
    # def test_api_can_delete_food(self):
    #     """Test the api can delete a food."""
    #     food = Food.objects.get()
    #     response = self.client.delete(
    #       reverse('details', kwargs={'pk': food.id}),
    #       format='json',
    #       follow=True)
    #     self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
