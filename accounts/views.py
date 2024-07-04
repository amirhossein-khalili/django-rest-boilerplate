from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserRegisterSerializer, UserSerializer


class UserRegister(APIView):

    serializer_class = UserRegisterSerializer

    def post(self, request):

        ser_data = UserRegisterSerializer(data=request.data)

        # check data is valid or not and create a new user
        if ser_data.is_valid():
            user = ser_data.create(ser_data.validated_data)

            return Response(
                {"message": "User created successfully", "user": ser_data.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ViewSet):
    """
    this is a view set that

    do crud operations on the

    users model
    """

    permission_classes = [IsAuthenticated, IsAdminUser]

    serializer_class = UserSerializer

    queryset = User.objects.all()

    def list(self, request):

        ser_data = UserSerializer(instance=self.queryset, many=True)

        return Response(data=ser_data.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        ser_data = UserSerializer(instance=user)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        ser_data = UserSerializer(instance=user, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_200_OK)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        user.is_active = False
        user.save()
        return Response(
            data={"message": "user deactivated "}, status=status.HTTP_200_OK
        )
