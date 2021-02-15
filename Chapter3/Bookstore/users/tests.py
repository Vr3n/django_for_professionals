from django.contrib.auth import get_user, get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .views import SignUpPageView
from .forms import CustomUserCreationForm

# Create your tests here.

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="Viren",
            email="virenpatel@gmail.com",
            password="Test@1234"
        )

        self.assertEqual(user.username, 'Viren')
        self.assertEqual(user.email, 'virenpatel@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superuser",
            email="superuser@gmail.com",
            password="test@1234"
        )

        self.assertEqual(admin_user.username, 'superuser')
        self.assertEqual(admin_user.email, 'superuser@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class SignUpPageTests(TestCase):

    def setUp(self) -> None:
        url = reverse('signup')
        self.response = self.client.get(url)

    # Test if signup page returns status code 200.
    def test_signuppage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    # Test if Signup Template is correct or not.
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/sign_up.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Home Page')


    # Check if CustomUserCreationForm is being used in the template.
    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    # testing if the signup view is used correctly.
    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignUpPageView.as_view().__name__
        )