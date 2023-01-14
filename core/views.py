from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import pyotp
from django.core.mail import send_mail
# Create your views here.

from rest_framework_simplejwt.views import TokenObtainPairView
 

class CustomLogin(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class OTPSerializer (serializers.Serializer):
    otp = serializers.CharField(max_length=6)


class OTPView (APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        global hotp

        hotp = pyotp.HOTP(pyotp.random_base32())

        otp = hotp.at(1)

        send_mail(
            subject='New OTP',
            message=f'Your OTP is : {otp}',
            from_email= 'blazingkrane@gmail.com',
            recipient_list=[request.user.email]
        )

        return Response({"Info": "otp sent"})

    def post(self, request):
        serializer = OTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        otp = serializer.validated_data['otp']
        if hotp.verify(otp, 1):

            user = request.user
            user.is_verified = True
            user.save()
            return Response({"success: 2FA successful "}, status=status.HTTP_202_ACCEPTED)

        return Response("error: invalid otp")
