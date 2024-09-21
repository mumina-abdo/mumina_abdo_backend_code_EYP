from django.test import TestCase
from shopping.models import Shopping_list, Shopping_list_item

class ShoppingListModelTests(TestCase):

    def setUp(self):
        self.shopping_list = Shopping_list.objects.create()

    def test_shopping_list_creation(self):
        self.assertEqual(self.shopping_list.shopping_list_id, 1)
        self.assertIsInstance(self.shopping_list, Shopping_list)

    def test_shopping_list_str(self):
        self.assertEqual(str(self.shopping_list), "1")

class ShoppingListItemModelTests(TestCase):

    def setUp(self):
        self.shopping_list = Shopping_list.objects.create()
        self.shopping_list_item = Shopping_list_item.objects.create(
            shopping_list_id=self.shopping_list,
            item="Apples",
            quantity=5,
            unit="kg"
        )

    def test_shopping_list_item_creation(self):
        self.assertEqual(self.shopping_list_item.shopping_list_item_id, 1)
        self.assertEqual(self.shopping_list_item.item, "Apples")
        self.assertEqual(self.shopping_list_item.quantity, 5)
        self.assertEqual(self.shopping_list_item.unit, "kg")
        self.assertIsInstance(self.shopping_list_item, Shopping_list_item)

    def test_shopping_list_item_str(self):
        expected_str = f"{self.shopping_list} Apples 5 kg"
        self.assertEqual(str(self.shopping_list_item), expected_str)


class ShoppingListItemModelRelationTests(TestCase):

    def setUp(self):
        self.shopping_list = Shopping_list.objects.create()

    def test_related_items_access(self):
        self.shopping_list_item1 = Shopping_list_item.objects.create(
            shopping_list_id=self.shopping_list,
            item="Bananas",
            quantity=3,
            unit="kg"
        )
        self.shopping_list_item2 = Shopping_list_item.objects.create(
            shopping_list_id=self.shopping_list,
            item="Oranges",
            quantity=2,
            unit="kg"
        )
        items = self.shopping_list.items.all()
        self.assertIn(self.shopping_list_item1, items)
        self.assertIn(self.shopping_list_item2, items)
        self.assertEqual(items.count(), 2)