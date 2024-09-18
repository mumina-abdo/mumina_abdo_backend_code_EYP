from django.test import TestCase
from .models import Category, FoodItem

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Fruits")

    def test_category_str(self):
        expected_string = f"{self.category.name} {self.category.updated_at}"
        self.assertEqual(str(self.category), expected_string)

class FoodItemModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Vegetables")
        self.food_item = FoodItem.objects.create(name="Carrot", quantity=10, category=self.category)

    def test_food_item_str(self):
        expected_string = f"{self.food_item.name} (Category: {self.food_item.category})"
        self.assertEqual(str(self.food_item), expected_string)

    def test_food_item_default_quantity(self):
        new_food_item = FoodItem.objects.create(name="Tomato", category=self.category)
        self.assertEqual(new_food_item.quantity, 0)

    def test_food_item_quantity(self):
        self.assertEqual(self.food_item.quantity, 10)
