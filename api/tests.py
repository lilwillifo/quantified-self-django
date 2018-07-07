from django.test import TestCase
from .models import Food

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
