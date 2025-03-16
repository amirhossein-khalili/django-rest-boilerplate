from django.test import TestCase

from accounts.models import User
from accounts.services.user_validation_impl import UserValidationServiceImpl


class UserValidationServiceImplTest(TestCase):

    def setUp(self):
        self.phone = "1234567890"
        self.user = User.objects.create_user(phone=self.phone)
        self.user_validation = UserValidationServiceImpl()

    def test_user_exists(self):
        self.assertTrue(self.user_validation.user_exists(self.phone))

        self.assertFalse(self.user_validation.user_exists("nonexistent_phone"))

    def test_has_user_access(self):
        self.assertTrue(self.user_validation.has_user_access(self.user))

        self.user.is_active = False
        self.user.save()
        self.assertFalse(self.user_validation.has_user_access(self.user))
