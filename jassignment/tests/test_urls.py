from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import index, fetch_data
class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_fetch_data_url_is_resolved(self):
        url = reverse('main:fetch_data', args=['test_postcode'])
        self.assertEquals(resolve(url).func, fetch_data)
