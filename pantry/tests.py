from django.test import TestCase
from django.core.exceptions import ValidationError
from ingredients.models import Ingredients
from .models import Pantry

class IngredientsModelTest(TestCase):

    def setUp(self):

        self.valid_ingredient = Ingredients.objects.create(
            ingredients_name="Flour",
            quantity=500,
            category="Baking"
        )

    def test_ingredients_creation(self):
        self.assertEqual(self.valid_ingredient.ingredients_name, "Flour")
        self.assertEqual(self.valid_ingredient.quantity, 500)
        self.assertEqual(self.valid_ingredient.category, "Baking")

    def test_ingredients_string_representation(self):
        self.assertEqual(str(self.valid_ingredient), "1 Flour")  

    def test_quantity_cannot_be_negative(self):
        negative_ingredient = Ingredients(ingredients_name="Sugar", quantity=-10, category="Baking")
        with self.assertRaises(ValidationError):  
            negative_ingredient.full_clean()

    def test_quantity_cannot_be_none(self):
        none_quantity_ingredient = Ingredients(ingredients_name="Butter", quantity=None, category="Dairy")
        with self.assertRaises(ValidationError):  
            none_quantity_ingredient.full_clean()


class PantryModelTest(TestCase):

    def setUp(self):

        self.ingredient = Ingredients.objects.create(
            ingredients_name="Flour",
            quantity=500,
            category="Baking"
        )

        self.pantry = Pantry.objects.create(
            quantity="2kg",
            item="Bread",
            users="testuser"
        )
        self.pantry.ingredient.add(self.ingredient)

    def test_pantry_creation(self):
        self.assertEqual(self.pantry.quantity, "2kg")
        self.assertEqual(self.pantry.item, "Bread")
        self.assertEqual(self.pantry.users, "testuser")
        self.assertIn(self.ingredient, self.pantry.ingredient.all())

    def test_string_representation(self):
        self.assertEqual(str(self.pantry), "2kg Bread")

    def test_pantry_links_to_ingredients(self):
        another_ingredient = Ingredients.objects.create(
            ingredients_name="Sugar",
            quantity=1000,
            category="Baking"
        )
        self.pantry.ingredient.add(another_ingredient)  
        self.assertIn(another_ingredient, self.pantry.ingredient.all())
        self.assertEqual(self.pantry.ingredient.count(), 2)  
        
    def test_quantity_field_max_length(self):
        pantry_item = Pantry(quantity="5kg", item="Rice", users="testuser")
        pantry_item.full_clean() 

        pantry_item.quantity = "A" * 21  
        with self.assertRaises(ValidationError): 
            pantry_item.full_clean()

    def test_item_field_max_length(self):
        pantry_item = Pantry(quantity="1kg", item="Salmon", users="testuser")
        pantry_item.full_clean()  

        pantry_item.item = "B" * 21 
        with self.assertRaises(ValidationError):  
            pantry_item.full_clean()

    def test_users_field_max_length(self):
        pantry_item = Pantry(quantity="1kg", item="Pasta", users="testuser")
        pantry_item.full_clean()  
        pantry_item.users = "C" * 21  
        with self.assertRaises(ValidationError):  
            pantry_item.full_clean()