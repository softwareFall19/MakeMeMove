import datetime
from django.test import TestCase
# from .forms import RegisterForm, ProfileForm
# from django import forms

# from .models import User

# def test_registration_form(self):
#     # test invalid data
#     invalid_data = {
#       "username": "user@test.com",
#       "firstname":"",
#       "lastname":"",
#       "email":"",
#       "password1": "secret",
#       "password2": "not secret"
#     }
#     form = RegisterForm(data=invalid_data)
#     form.is_valid()
#     self.assertTrue(form.errors)

#     valid_data = {
#        "username": "user@test.com",
#       "firstname":"",
#       "lastname":"",
#       "email":"",
#       "password1": "secret",
#       "password2": "not secret"
#     }
#     form = RegistrationForm(data=valid_data)
#     form.is_valid()
#     self.assertFalse(form.errors)


# def test_login_form(self):
#     # test invalid data
#     invalid_data = {
#       "username": "user@test.com",
#       "password": "not secret"
#     }
#     form = LoginForm(data=invalid_data)
#     form.is_valid()
#     self.assertTrue(form.errors)

#     valid_data = {
#       "username": "user@test.com",
#       "password": "not secret"
#     }
#     form = LoginForm(data=valid_data)
#     form.is_valid()
#     self.assertFalse(form.errors)

# tests for models
# class UserTestCase(TestCase):
#     def setUp(self):
#         self.author = User.objects.create(
#           username='author@test.com',
#           email='author@test.com',
#           user_type=User.AUTHOR
#         )
#         self.publisher = User.objects.create(
#           username='publisher@test.com',
#           email='publisher@test.com',
#           user_type=User.AUTHOR
#         )

#     def test_create_user_profile(self):
#       self.assertEqual(User.get_authors(), 1)

#     def test_save_user_profile(self):
#       self.assertTrue(self.author.can_write_books())
#       self.assertFalse(self.publisher.can_write_books())
