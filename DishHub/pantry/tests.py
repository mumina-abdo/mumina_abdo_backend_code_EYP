from django.test import TestCase
from .models import Pantry

class PantryModelTest(TestCase):
    def setUp(self):
        self.pantry_item = Pantry.objects.create(quantity="500g", item="Salt")

    def test_pantry_creation(self):
        self.assertEqual(self.pantry_item.quantity, "500g")
        self.assertEqual(self.pantry_item.item, "Salt")

    def test_pantry_str_method(self):
        self.assertEqual(str(self.pantry_item), "500g Salt")

    def test_pantry_max_length(self):
        max_length_quantity = self.pantry_item._meta.get_field('quantity').max_length
        max_length_item = self.pantry_item._meta.get_field('item').max_length
        self.assertEqual(max_length_quantity, 20)
        self.assertEqual(max_length_item, 20)

    def test_pantry_id_auto_increment(self):
        new_pantry_item = Pantry.objects.create(quantity="250g", item="Sugar")
        self.assertEqual(new_pantry_item.id, self.pantry_item.id + 1)

    def test_pantry_ingredient_field_exists(self):
        self.assertTrue(hasattr(self.pantry_item, 'ingredient'))
# Create your tests here.
