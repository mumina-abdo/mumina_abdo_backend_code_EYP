from django.test import TestCase
from .models import Ingredients
from django.core.exceptions import ValidationError

class IngredientsModelTest(TestCase):
    def setUp(self):
        self.ingredient = Ingredients.objects.create(
            ingredients_name='Tomato',
            quantity=10
        )

    def test_ingredient_creation(self):
        self.assertEqual(self.ingredient.ingredients_name, 'Tomato')
        self.assertEqual(self.ingredient.quantity, 10)

    def test_string_representation(self):
        self.assertEqual(str(self.ingredient), f"{self.ingredient.ingredients_id} Tomato")

    def test_ingredient_update(self):
        self.ingredient.quantity = 15
        self.ingredient.save()
        self.assertEqual(self.ingredient.quantity, 15)

    def test_ingredient_deletion(self):
        ingredient_id = self.ingredient.ingredients_id
        self.ingredient.delete()
        with self.assertRaises(Ingredients.DoesNotExist):
            Ingredients.objects.get(ingredients_id=ingredient_id)

    def test_ingredient_quantity_negative(self):
        ingredient = Ingredients(ingredients_name='Lettuce', quantity=-5)
        with self.assertRaises(ValidationError):
            ingredient.full_clean()