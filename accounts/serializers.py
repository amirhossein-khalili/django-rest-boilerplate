from django.contrib.auth.models import User
from rest_framework import serializers


def clean_email(value):
    if "admin" in value:
        raise serializers.ValidationError("Email can't contain 'admin'!!")


class UserRegisterSerializer(serializers.ModelSerializer):
    repeat_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "email", "repeat_password")
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"validators": [clean_email]},
        }

    def create(self, validated_data):
        validated_data.pop("repeat_password")
        user = User.objects.create_user(**validated_data)
        return user

    def validate_username(self, value):
        if value.lower() == "admin":
            raise serializers.ValidationError("Username can't be 'admin'!!")
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken!!")
        return value

    def validate(self, data):
        if data["password"] != data["repeat_password"]:
            raise serializers.ValidationError(
                "Password and repeat password must match!!"
            )
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
