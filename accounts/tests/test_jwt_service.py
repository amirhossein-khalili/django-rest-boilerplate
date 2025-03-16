from unittest.mock import MagicMock

from django.test import TestCase
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import User
from accounts.services.jwt_service_impl import JWTServiceImpl


class JWTServiceImplTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(phone="1234567890")
        self.jwt_service = JWTServiceImpl()

    def test_generate_token(self):
        tokens = self.jwt_service.generate_token(self.user)

        self.assertIn("access", tokens)
        self.assertIn("refresh", tokens)
        self.assertIsInstance(tokens["access"], str)
        self.assertIsInstance(tokens["refresh"], str)

    def test_verify_token_valid(self):
        tokens = self.jwt_service.generate_token(self.user)
        valid_token = tokens["access"]

        validated_token = self.jwt_service.verify_token(valid_token)
        self.assertEqual(str(validated_token["user_id"]), str(self.user.id))

    def test_verify_token_invalid(self):
        with self.assertRaises(Exception):
            self.jwt_service.verify_token("invalid_token")
