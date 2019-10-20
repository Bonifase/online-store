import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..user.models import UserProfile
from ..user.serializers import UserSerializer


# initialize the APIClient app
client = Client()

class CreateNewProfileTest(TestCase):
    """ Test module for inserting a new puppy """

    def setUp(self):
        self.valid_payload = {
            'name': 'Muffin',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }

    def test_create_valid_user(self):
        response = client.post(
            reverse('UserViewSet'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

