from django.test import TestCase
from .models import ShoppingList, ShoppingListItem


class ShoppingListModelTest(TestCase):

    def setUp(self):
        self.shopping_list = ShoppingList.objects.create(shopping_list_name='Groceries')

    def test_shopping_list_creation(self):
        self.assertIsInstance(self.shopping_list, ShoppingList)
        self.assertEqual(self.shopping_list.shopping_list_name, 'Groceries')
        self.assertIsNotNone(self.shopping_list.date_created)

    def test_str_method(self):
        expected_str = f'Groceries (ID: {self.shopping_list.shopping_list_id})'
        self.assertEqual(str(self.shopping_list), expected_str)


class ShoppingListItemModelTest(TestCase):

    def setUp(self):
        self.shopping_list = ShoppingList.objects.create(shopping_list_name='Groceries')
        self.shopping_list_item = ShoppingListItem.objects.create(
            shopping_list=self.shopping_list,
            item='Apples',
            quantity=5,
            unit='kg'
        )

    def test_shopping_list_item_creation(self):
        self.assertIsInstance(self.shopping_list_item, ShoppingListItem)
        self.assertEqual(self.shopping_list_item.item, 'Apples')
        self.assertEqual(self.shopping_list_item.quantity, 5)
        self.assertEqual(self.shopping_list_item.unit, 'kg')
        self.assertEqual(self.shopping_list_item.shopping_list, self.shopping_list)

    def test_str_method(self):
        expected_str = f'Apples (Quantity: {self.shopping_list_item.quantity}, Unit: {self.shopping_list_item.unit})'
        self.assertEqual(str(self.shopping_list_item), expected_str)
