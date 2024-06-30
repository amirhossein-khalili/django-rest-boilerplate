from django.contrib.auth.models import User
from rest_framework import serializers


def clean_email(value):
    if "admin" in value:
        raise serializers.ValidationError("Email can't contain 'admin'!!")


class UserRegisterSerializer(serializers.Serializer):

    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[clean_email])
    password = serializers.CharField(required=True, write_only=True)
    repeat_password = serializers.CharField(required=True, write_only=True)

    def validate_username(self, value):
        if value == "admin":
            raise serializers.ValidationError("Username can't be 'admin'!!")
        user = User.objects.filter(username=value)
        print(user)
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken!!")

        return value

    def validate(self, data):
        if data["password"] != data["repeat_password"]:
            raise serializers.ValidationError(
                "Password and repeat password must match!!"
            )
        return data
