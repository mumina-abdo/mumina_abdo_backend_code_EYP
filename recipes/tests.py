from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):

    def setUp(self):
        self.recipe = Recipe.objects.create(
            recipe_id="1",
            title="Chocolate Cake",
            instructions="Mix ingredients and bake."
        )

    def test_string_representation(self):
        expected_string = self.recipe.title
        self.assertEqual(str(self.recipe), expected_string)

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.recipe_id, "1")
        self.assertEqual(self.recipe.title, "Chocolate Cake")
        self.assertEqual(self.recipe.instructions, "Mix ingredients and bake.")

