from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserRegisterSerializer


class UserRegister(APIView):

    def post(self, request):

        ser_data = UserRegisterSerializer(data=request.data)

        # check data is valid or not
        if ser_data.is_valid():

            User.objects.create_user(
                username=ser_data.validated_data["username"],
                email=ser_data.validated_data["email"],
                password=ser_data.validated_data["password"],
            )

            return Response(
                {"message": "User created successfully", "user": ser_data.data}
            )

        return Response(ser_data.errors)
