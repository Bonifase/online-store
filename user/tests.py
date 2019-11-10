import json
from . import models
from . import data
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
UserProfile = models.UserProfile


class UserRegistrationAPIViewTestCase(APITestCase):
    url = "http://127.0.0.1:8000/api/profile/"

    def test_invalid_password_registration(self):
        """
        Test to verify that a post call with invalid passwords
        """
        response = self.client.post(self.url, data.user_data_0)
        self.assertEqual(400, response.status_code)

    def test_user_registration(self):
        """
        Test to verify that a post call with user valid data
        """
        response = self.client.post(self.url, data.user_data)
        self.assertEqual(201, response.status_code)
        self.assertTrue("name" in json.loads(response.content))

    def test_without_name_key(self):
        """
        Test to verify that a post with blank name key is rejected
        """
        response = self.client.post(self.url, data.user_data_1)
        result = json.loads(response.content)
        self.assertEqual(result['name'][0], 'This field is required.')

    def test_without_email_key(self):

        response = self.client.post(self.url, data.user_data_2)
        result = json.loads(response.content)
        self.assertEqual(result['email'][0], 'This field is required.')

    def test_without_password_key(self):
        response = self.client.post(self.url, data.user_data_3)
        result = json.loads(response.content)
        self.assertEqual(result['password'][0], 'This field is required.')

    def test_without_name_value(self):
        response = self.client.post(self.url, data.user_data_4)
        result = json.loads(response.content)
        self.assertEqual(result['name'][0], 'This field may not be blank.')

    def test_without_email_value(self):

        response = self.client.post(self.url, data.user_data_5)
        result = json.loads(response.content)
        self.assertEqual(
            result['email'][0], 'This field may not be blank.')
    
    def test_without_password_value(self):

        response = self.client.post(self.url, data.user_data_6)
        result = json.loads(response.content)
        self.assertEqual(
            result['password'][0], 'This field may not be blank.')
    
    def test_with_all_blank_fields(self):
        """
        Test to verify that a post with blank fields is rejected
        """
        response = self.client.post(self.url, data.user_data_7)
        result = json.loads(response.content)
        self.assertEqual(result['name'][0], 'This field may not be blank.')
        self.assertEqual(result['email'][0], 'This field may not be blank.')
        self.assertEqual(result['password'][0], 'This field may not be blank.')


class UserLoginAPIViewTestCase(APITestCase):
    url = 'http://127.0.0.1:8000/api/login/'

    def setUp(self):
        self.name = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = UserProfile.objects.create_user(
            self.name, self.email, self.password)

    def test_authentication_without_password(self):
        response = self.client.post(self.url, {"name": "snowman"})
        self.assertEqual(400, response.status_code)

    def test_authentication_with_wrong_password(self):
        response = self.client.post(
            self.url, {"name": self.name, "password": "I_know"})
        self.assertEqual(400, response.status_code)

    def test_authentication_with_valid_data(self):
        response = self.client.post(
            self.url, {"username": self.name, "password": self.password})
        self.assertEqual(200, response.status_code)
        self.assertTrue("token" in json.loads(response.content))
