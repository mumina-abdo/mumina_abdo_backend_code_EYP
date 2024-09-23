from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Ingredients

class IngredientsModelTest(TestCase):

    def setUp(self):
        self.ingredient = Ingredients.objects.create(
            ingredients_name="Sugar",
            quantity=5
        )

    def test_string_representation(self):
        expected_string = f"{self.ingredient.ingredients_id} Sugar"
        self.assertEqual(str(self.ingredient), expected_string)

    def test_ingredient_creation(self):
        self.assertEqual(self.ingredient.ingredients_name, "Sugar")
        self.assertEqual(self.ingredient.quantity, 5)

    def test_quantity_cannot_be_negative(self):
        ingredient = Ingredients(ingredients_name="Salt", quantity=-1)
        with self.assertRaises(ValidationError):
            ingredient.full_clean()  

    def test_quantity_cannot_be_none(self):
        ingredient = Ingredients(ingredients_name="Pepper", quantity=None)
        with self.assertRaises(ValidationError):
            ingredient.full_clean()  
