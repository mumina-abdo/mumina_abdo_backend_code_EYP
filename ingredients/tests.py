from django.test import TestCase
from django.core.exceptions import ValidationError
from ingredients.models import Ingredients
from categories.models import Category  
class IngredientsModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Baking")  
        self.valid_ingredient = Ingredients.objects.create(
            ingredients_name="Flour",
            quantity=500
        )
        self.valid_ingredient.categories.add(self.category) 

    def test_ingredients_creation(self):
        self.assertEqual(self.valid_ingredient.ingredients_name, "Flour")
        self.assertEqual(self.valid_ingredient.quantity, 500)
        self.assertTrue(self.category in self.valid_ingredient.categories.all()) 

    def test_ingredients_string_representation(self):
        self.assertEqual(str(self.valid_ingredient), f"{self.valid_ingredient.ingredients_id} {self.valid_ingredient.ingredients_name}")

    def test_quantity_cannot_be_negative(self):
        negative_ingredient = Ingredients(ingredients_name="Sugar", quantity=-10)
        with self.assertRaises(ValidationError):
            negative_ingredient.full_clean()

    def test_quantity_cannot_be_none(self):
        none_quantity_ingredient = Ingredients(ingredients_name="Butter", quantity=None)
        with self.assertRaises(ValidationError):
            none_quantity_ingredient.full_clean()

    def test_quantity_validation(self):
        valid_ingredient = Ingredients.objects.create(ingredients_name="Carrot", quantity=100)
        valid_ingredient.categories.add(self.category)
        
        invalid_ingredient = Ingredients(ingredients_name="Carrot", quantity=-50)
        with self.assertRaises(ValidationError):
            invalid_ingredient.full_clean()




