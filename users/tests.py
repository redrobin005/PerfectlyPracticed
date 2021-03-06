from django.http import response
from django.test import TestCase
from django.urls import resolve

from users.models import MyUser

# Create your tests here.
class RegisterLoginTest(TestCase):

    def sign_up_post(self):
        response = self.client.post('/sign_up', data={'email': 
        'user2@test.com', 'first_name':'User', 'last_name':'Test',
        'password1':'PassTest123', 'password2':'PassTest123'})
        return response

    def sign_up_and_login(self):
        self.client.post('/sign_up', data={'email': 
        'user2@test.com', 'first_name':'User', 'last_name':'Test',
        'password1':'PassTest123', 'password2':'PassTest123'})
        response = self.client.post('/', data={'username': 
        'user2@test.com','password':'PassTest123'})
        return response

    def test_uses_login_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'users/base_auth_login.html')

    def test_uses_sign_up_template(self):
        response = self.client.get('/sign_up')
        self.assertTemplateUsed(response, 'users/base_auth_signup.html')
    
    def test_details_saved_after_post(self):
        self.sign_up_post()
        self.assertEqual(MyUser.objects.count(), 1)
        new_item = MyUser.objects.first()
        self.assertEqual(new_item.email, 'user2@test.com')
        self.assertEqual(new_item.first_name, 'User')
        self.assertEqual(new_item.last_name, 'Test')
        self.assertTrue(new_item.check_password('PassTest123'))

    def test_redirect_to_login_after_signup(self):
        response = self.sign_up_post()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_successful_login(self):
        response = self.sign_up_and_login()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/login_success')
    
    

    
        
