from django.test import TestCase
from .models import ShoppingList, ShoppingListItem

class ShoppingListModelTest(TestCase):

    def setUp(self):
        self.shopping_list = ShoppingList.objects.create(
            shopping_list_name="Grocery List"
        )

    def test_string_representation(self):
        expected_string = f"{self.shopping_list.shopping_list_name} (ID: {self.shopping_list.shopping_list_id})"
        self.assertEqual(str(self.shopping_list), expected_string)

    def test_shopping_list_creation(self):
        self.assertEqual(self.shopping_list.shopping_list_name, "Grocery List")
        self.assertIsNotNone(self.shopping_list.date_created)


class ShoppingListItemModelTest(TestCase):

    def setUp(self):
        self.shopping_list = ShoppingList.objects.create(
            shopping_list_name="Grocery List"
        )
        self.shopping_list_item = ShoppingListItem.objects.create(
            shopping_list=self.shopping_list,
            item="Milk",
            quantity=2,
            unit="liters"
        )

    def test_string_representation(self):
        expected_string = f"{self.shopping_list_item.item} (Quantity: {self.shopping_list_item.quantity}, Unit: {self.shopping_list_item.unit})"
        self.assertEqual(str(self.shopping_list_item), expected_string)

    def test_shopping_list_item_creation(self):
        self.assertEqual(self.shopping_list_item.item, "Milk")
        self.assertEqual(self.shopping_list_item.quantity, 2)
        self.assertEqual(self.shopping_list_item.unit, "liters")
        self.assertEqual(self.shopping_list_item.shopping_list, self.shopping_list)
