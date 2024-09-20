from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            recipe_id='1',
            title='Test Recipe',
            ingredients='Ingredient 1, Ingredient 2',
            instructions='Test instructions.',
            image_url='http://example.com/image.jpg'
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.title, 'Test Recipe')
        self.assertEqual(self.recipe.ingredients, 'Ingredient 1, Ingredient 2')
        self.assertEqual(self.recipe.instructions, 'Test instructions.')
        self.assertEqual(self.recipe.image_url, 'http://example.com/image.jpg')

    def test_string_representation(self):
        self.assertEqual(str(self.recipe), 'Test Recipe Ingredient 1, Ingredient 2')

    def test_blank_ingredients(self):
        blank_recipe = Recipe.objects.create(
            recipe_id='2',
            title='Another Recipe',
            ingredients='',
            instructions='Some instructions.',
            image_url='http://example.com/image2.jpg'
        )
        self.assertEqual(blank_recipe.ingredients, '')

    def test_null_image_url(self):
        null_image_recipe = Recipe.objects.create(
            recipe_id='3',
            title='Null Image Recipe',
            ingredients='Ingredient 1',
            instructions='Instructions.',
            image_url=None
        )
        self.assertIsNone(null_image_recipe.image_url)
