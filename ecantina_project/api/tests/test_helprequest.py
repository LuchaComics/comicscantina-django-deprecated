from django.core.urlresolvers import resolve
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf.urls.static import static, settings
from api.models.ec.helprequest import HelpRequest
from inventory_base.tests.sample import SampleDataPopulator
from rest_framework.test import APIClient, force_authenticate
from rest_framework import status


# Contants
TEST_USER_EMAIL = "ledo@gah.com"
TEST_USER_USERNAME = TEST_USER_EMAIL
TEST_USER_PASSWORD = "password"

# Extra parameters to make this a Ajax style request.
KWARGS = {'HTTP_X_REQUESTED_WITH':'XMLHttpRequest'}


class HelpTestCase(TestCase):
    """
        Run in Console:
        python manage.py test api.tests.test_helprequest
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
    
    def test_post_with_success(self):
        user = User.objects.get(username=TEST_USER_USERNAME)
        client = APIClient()
        client.force_authenticate(user=user)
        
        response = client.post('/api/helprequests/', {
            'subject': 2,
            'subject_url': "http://www.comicscantina.com",
            'message': "This is a test",
            'employee': 1,
            'store': 1,
            'organization': 1,
        }, format='json')
        
        #print("", response.data)  # Used for debugging purposes only.
        
        # Verify that our object was created.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify the correct data was inputted
        self.assertEqual(response.data['subject'], 2)
        self.assertEqual(response.data['organization'], 1)
        self.assertEqual(response.data['employee'], 1)

        # Verify our database has been modified.
        self.assertEqual(HelpRequest.objects.count(), 1)
        self.assertEqual(HelpRequest.objects.get().message, 'This is a test')
