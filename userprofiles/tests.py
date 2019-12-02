from django.http import HttpRequest
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile
from  . import views
from django.contrib.auth import get_user_model
from django.forms import forms
from .forms import RegisterForm, LoginForm


class SignUpPageTests(SimpleTestCase):

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'userprofiles/signup.html')
     
    

class SignInPageTests(TestCase):

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signin'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signin'))
        # print(response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'userprofiles/signin.html')

    def test_signin(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

        c = Client()
        logged_in = c.login(username='testuser', password='12345')
        self.assertTrue(logged_in) 

    def test_signout(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

        c = Client()
        logged_in = c.login(username='testuser', password='12345')
        # logged_out = c.logout()
        # self.assertEqual(logged_out, None)
        

class UserHomePageTestCase(TestCase):
    
    def test_view_url_by_name(self):
        response = self.client.get(reverse('user_home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('user_home'))
        # print(response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'userprofiles/user_home.html')

class RegistrationViewTestCase(TestCase):
    def setUp(self):
        self.sample_user = User.objects.create(username='alice')
        self.sample_user.set_password("secret")
        self.sample_userprofile = Profile.objects.create(user_id=self.sample_user.id)

    def test_existing_username(self):
        response = self.client.post(reverse('signup'),
                                    data={ 'username': 'alice', # Will fail on username uniqueness.
                                           'email': 'foo@example.com',
                                           'password1': 'Qwerty123!',
                                           'password2': 'Qwerty123!' })
        #print(response)                                  
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['form'])
        self.assertTrue(response.context['form'].errors)

class RegistrationFormTests(TestCase):
    def setUp(self):
        self.sample_user = User.objects.create(username='alice')
        self.sample_user.set_password("secret")
        self.sample_userprofile = Profile.objects.create(user_id=self.sample_user.id)

    def test_register_form_for_invalid_data(self):
        invalid_data_dicts = [
            # Non-alphanumeric username.
            {
            'data':
            { 'username': '~~~~~',
              'email': 'foo@example.com',
              'password1': 'foo',
              'password2': 'foo' },
            'error':
            ('username', [u"Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters."])
            },
            # Already-existing username.
            {
            'data':
            { 'username': 'alice',
              'email': 'alice@example.com',
              'password1': 'secret',
              'password2': 'secret' },
            'error':
            ('username', [u"A user with that username already exists."])
            },
            # Mismatched passwords.
            {
            'data':
            { 'username': 'foo',
              'email': 'foo@example.com',
              'password1': 'foo',
              'password2': 'bar' },
            'error':
            ('password2', [u"The two password fields didn't match."])
            },
            ]

        for invalid_dict in invalid_data_dicts:
            form = RegisterForm(data=invalid_dict['data'])
            self.assertFalse(form.is_valid())
            self.assertEqual(form.errors[invalid_dict['error'][0]], invalid_dict['error'][1])

    def test_register_form_for_valid_data(self):
            valid_data = { 'data':
            { 'username': 'div123',
              'email': 'foo@example.com',
              'password1': 'Qwerty123!',
              'password2': 'Qwerty123!' 
            },
            }

            form = RegisterForm(data=valid_data['data'])
            print(form.is_valid())
            self.assertTrue(form.is_valid())
