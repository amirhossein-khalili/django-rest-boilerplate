# accounts/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import OTPSerializer
from .services.auth_facade import AuthenticationFacade


class AuthenticationView(APIView):

    def __init__(self):
        self.otp_service = OTPServiceImpl()
        self.jwt_service = JWTServiceImpl()
        self.user_validation = UserValidationServiceImpl()

    """
    A single endpoint for both OTP-based signup and login.
    This view leverages the Strategy pattern by delegating specific tasks (e.g., OTP handling, JWT generation)
    to interchangeable service implementations, and the Facade pattern to simplify the authentication workflow.
    """

    def post(self, request):
        """
        Handle POST requests for OTP requests or verification.
        - If only 'phone' is provided, an OTP is sent.
        - If both 'phone' and 'otp' are provided, verify OTP and either sign up or log in the user.

        Strategy Pattern: The AuthenticationFacade uses pluggable strategies (OTPServiceImpl, JWTServiceImpl)
        to abstract the details of OTP generation/verification and token creation.
        Facade Pattern: The AuthenticationFacade provides a unified interface, hiding the complexity of
        user creation, OTP validation, and token generation from the view.
        """

        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():

            phone = serializer.validated_data["phone"]
            otp = serializer.validated_data.get("otp")

            auth_facade = AuthenticationFacade()

            if otp:

                try:

                    # Case 1: OTP is provided - attempt verification and authentication
                    # Delegate to the facade to verify OTP and either create a user or log in
                    # The facade internally uses strategies (OTPServiceImpl for OTP, JWTServiceImpl for tokens)

                    result = auth_facade.verify_otp_and_authenticate(phone, otp)
                    return Response(result, status=status.HTTP_200_OK)
                except ValueError as e:
                    return Response(
                        {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
                    )

            else:

                # Case 2: No OTP provided - request a new OTP for the phone number
                # The facade uses OTPServiceImpl (strategy) to generate and send the OTP

                result = auth_facade.request_otp(phone)
                return Response(result, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
