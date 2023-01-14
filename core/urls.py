from django.urls import path
from .views import OTPView, CustomLogin


urlpatterns = [
    
    # path('otp' OTPView.as_view()),
    path('login', CustomLogin.as_view() ),
    path ('otp', OTPView.as_view())
]
