from django.test import TestCase, Client
from django.urls import reverse
from main.models import Location
import json
from main.views import format_data
from unittest.mock import patch
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.fetch_data_url = reverse('main:fetch_data', args=['test_postcode'])

    def test_index_view(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'main/index.html')

    @patch('main.views.requests.get')
    def test_fetch_data_view(self, mock_get):
        Location.objects.create(postcode='test_postcode', name='test')
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'restaurants': [
                {'name': 'Restaurant 1', 'rating': {'count': 5}, 'cuisines': 'Italian', 'address': '123 Main St'},
                {'name': 'Restaurant 2', 'rating': {'count': 4}, 'cuisines': 'Mexican', 'address': '456 Elm St'},
                {'name': 'Restaurant 3', 'rating': {'count': 5}, 'cuisines': 'Italian', 'address': '123 Main St'},
                {'name': 'Restaurant 4', 'rating': {'count': 4}, 'cuisines': 'Mexican', 'address': '456 Elm St'},
                {'name': 'Restaurant 5', 'rating': {'count': 5}, 'cuisines': 'Italian', 'address': '123 Main St'},
                {'name': 'Restaurant 6', 'rating': {'count': 4}, 'cuisines': 'Mexican', 'address': '456 Elm St'},
                {'name': 'Restaurant 7', 'rating': {'count': 5}, 'cuisines': 'Italian', 'address': '123 Main St'},
                {'name': 'Restaurant 8', 'rating': {'count': 4}, 'cuisines': 'Mexican', 'address': '456 Elm St'},
                {'name': 'Restaurant 9', 'rating': {'count': 5}, 'cuisines': 'Italian', 'address': '123 Main St'},
                {'name': 'Restaurant 10', 'rating': {'count': 4}, 'cuisines': 'Mexican', 'address': '456 Elm St'}

            ]
        }

        response = self.client.get(self.fetch_data_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')

    def test_format_data(self):
        sample_data = {
            'restaurants': [
                {'name': 'Restaurant 1', 'rating': {'count': 5}, 'cuisines': 'Italian', 'address': '123 Main St'},
                {'name': 'Restaurant 2', 'rating': {'count': 4}, 'cuisines': 'Mexican', 'address': '456 Elm St'},
                {'name': 'Restaurant 3', 'rating': {'count': 5}, 'cuisines': 'Italian', 'address': '123 Main St'},
                {'name': 'Restaurant 4', 'rating': {'count': 4}, 'cuisines': 'Mexican', 'address': '456 Elm St'},
                {'name': 'Restaurant 5', 'rating': {'count': 5}, 'cuisines': 'Italian', 'address': '123 Main St'},
                {'name': 'Restaurant 6', 'rating': {'count': 4}, 'cuisines': 'Mexican', 'address': '456 Elm St'},
                {'name': 'Restaurant 7', 'rating': {'count': 5}, 'cuisines': 'Italian', 'address': '123 Main St'},
                {'name': 'Restaurant 8', 'rating': {'count': 4}, 'cuisines': 'Mexican', 'address': '456 Elm St'},
                {'name': 'Restaurant 9', 'rating': {'count': 5}, 'cuisines': 'Italian', 'address': '123 Main St'},
                {'name': 'Restaurant 10', 'rating': {'count': 4}, 'cuisines': 'Mexican', 'address': '456 Elm St'}

            ]
        }

        formatted_data = format_data(sample_data)

        expected_data = {
            'Restaurant 1': {'rating': 5, 'cuisines': 'Italian', 'address': '123 Main St'},
            'Restaurant 2': {'rating': 4, 'cuisines': 'Mexican', 'address': '456 Elm St'},
            'Restaurant 3': {'rating': 5, 'cuisines': 'Italian', 'address': '123 Main St'},
            'Restaurant 4': {'rating': 4, 'cuisines': 'Mexican', 'address': '456 Elm St'},
            'Restaurant 5': {'rating': 5, 'cuisines': 'Italian', 'address': '123 Main St'},
            'Restaurant 6': {'rating': 4, 'cuisines': 'Mexican', 'address': '456 Elm St'},
            'Restaurant 7': {'rating': 5, 'cuisines': 'Italian', 'address': '123 Main St'},
            'Restaurant 8': {'rating': 4, 'cuisines': 'Mexican', 'address': '456 Elm St'},
            'Restaurant 9': {'rating': 5, 'cuisines': 'Italian', 'address': '123 Main St'},
            'Restaurant 10': {'rating': 4, 'cuisines': 'Mexican', 'address': '456 Elm St'},

        }

        self.assertEqual(formatted_data, expected_data)




