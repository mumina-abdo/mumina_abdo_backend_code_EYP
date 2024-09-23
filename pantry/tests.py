from django.test import TestCase
from .models import Pantry

class PantryModelTest(TestCase):

    def setUp(self):
        self.pantry_item = Pantry.objects.create(
            quantity="2",
            item="Sugar"
        )

    def test_string_representation(self):
        expected_string = f"{self.pantry_item.quantity} {self.pantry_item.item}"
        self.assertEqual(str(self.pantry_item), expected_string)

    def test_pantry_creation(self):
        self.assertEqual(self.pantry_item.quantity, "2")
        self.assertEqual(self.pantry_item.item, "Sugar")
