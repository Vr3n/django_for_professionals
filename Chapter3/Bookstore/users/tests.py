from django.contrib.auth import get_user, get_user_model
from django.test import TestCase

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