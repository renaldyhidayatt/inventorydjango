from django.test import TestCase
from .models import Category


# Create your tests here.
class CategoryTestCase(TestCase):
    def setUp(self):
        cat = Category.objects.create(name='test')
        self.cat = cat

    def test_category_name(self):
        self.assertEqual(self.cat.name, 'test')