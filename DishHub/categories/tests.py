from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Category, FoodItem

class CategoryModelTests(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Fruits")
        self.assertIsInstance(category, Category)
        self.assertEqual(category.name, "Fruits")

    def test_category_name_max_length(self):
        with self.assertRaises(ValidationError): 
            category = Category(name="A" * 101)
            category.full_clean()

class FoodItemModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Fruits")

    def test_food_item_creation(self):
        food_item = FoodItem.objects.create(name="Apple", category=self.category)
        self.assertIsInstance(food_item, FoodItem)
        self.assertEqual(food_item.name, "Apple")
        self.assertEqual(food_item.category, self.category)
        self.assertEqual(food_item.quantity, 0)

    def test_food_item_name_max_length(self):
        with self.assertRaises(ValidationError):
            food_item = FoodItem(name="A" * 101, category=self.category)
            food_item.full_clean()
    
    def test_food_item_quantity_default(self):
        food_item = FoodItem.objects.create(name="Banana", category=self.category)
        self.assertEqual(food_item.quantity, 0)
    
    def test_food_item_category_cascade(self):
        food_item = FoodItem.objects.create(name="Orange", category=self.category)
        self.category.delete()
        with self.assertRaises(FoodItem.DoesNotExist):
            FoodItem.objects.get(pk=food_item.pk)
 