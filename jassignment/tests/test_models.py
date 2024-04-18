from django.test import TestCase
from main.models import Location
class TestModels(TestCase):
    def setUp(self):
        self.location = Location.objects.create(postcode='test_postcode', name='test_name')

    def test_location_creation(self):
        self.assertEqual(self.location.postcode, 'test_postcode')
        self.assertEqual(self.location.name, 'test_name')

