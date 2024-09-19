from django.forms import ValidationError
from django.test import TestCase
from .models import Ingredients

class IngredientsTestCase(TestCase):

    def setUp(self):
        self.valid_ingredient = Ingredients.objects.create(
            ingredients_name="Rice",
            quantity=100,
            category="Grains"
        )


    def test_ingredients_model_without_quantity(self):
        ingredient = Ingredients()
        ingredient.ingredients_name = "Test Ingredient"
        ingredient.category = "Fruit"

        with self.assertRaises(ValidationError):
            ingredient.full_clean()

        ingredient.quantity = 50
        ingredient.full_clean()

    def test_ingredients_model_without_category(self):
        ingredient = Ingredients()
        ingredient.ingredients_name = "Test Ingredient"
        ingredient.quantity = 50

        with self.assertRaises(ValidationError):
            ingredient.full_clean()

        ingredient.category = "Fruit"
        ingredient.full_clean()

    def test_quantity_validation(self):
        self.assertEqual(self.valid_ingredient.quantity, 100)

        invalid_ingredient = Ingredients(ingredients_name="Carrot", quantity=-50, category="Vegetables")
        with self.assertRaises(ValidationError):
            invalid_ingredient.full_clean()

        invalid_ingredient.quantity = None
        with self.assertRaises(ValidationError):
            invalid_ingredient.full_clean()

