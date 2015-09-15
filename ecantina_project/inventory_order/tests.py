from django.core.urlresolvers import resolve
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf.urls.static import static, settings
from . import views
from inventory_base.tests.sample import SampleDataPopulator


# Contants
TEST_USER_EMAIL = "ledo@gah.com"
TEST_USER_USERNAME = TEST_USER_EMAIL
TEST_USER_PASSWORD = "password"

# Extra parameters to make this a Ajax style request.
KWARGS = {'HTTP_X_REQUESTED_WITH':'XMLHttpRequest'}


class OrderTestCase(TestCase):
    """
        Run in Console:
        python manage.py test inventory_order.tests
    """
    def tearDown(self):
        pass
        # Clear Sample Data
        populator = SampleDataPopulator()
        populator.dealloc()
    
    def setUp(self):
        # Create Sample Data
        populator = SampleDataPopulator()
        populator.populate()
    
    def test_url_resolves_to_orders_page(self):
        found = resolve('/inventory/1/1/orders')
        self.assertEqual(found.func, views.orders_page)
    
    def test_url_resolves_to_order_details_page(self):
        found = resolve('/inventory/1/1/orders/1/')
        self.assertEqual(found.func, views.order_details_page)
    
    def test_orders_page_returns_correct_html(self):
        client = Client()
        client.login(
            username=TEST_USER_USERNAME,
            password=TEST_USER_PASSWORD
        )
        response = client.post('/inventory/1/1/orders')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Orders',response.content)
        self.assertIn(b'View All',response.content)

    def test_orders_details_page_returns_correct_html(self):
        client = Client()
        client.login(
            username=TEST_USER_USERNAME,
            password=TEST_USER_PASSWORD
        )
        response = client.post('/inventory/1/1/orders/1/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Orders',response.content)
        self.assertIn(b'Details',response.content)