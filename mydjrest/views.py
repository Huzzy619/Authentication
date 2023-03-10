from django.shortcuts import render, redirect
from .serializers import CustomSocialLoginSerializer
# from auth.


from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
import requests


class CustomSocialLoginView(SocialLoginView):
    serializer_class = CustomSocialLoginSerializer


# if you want to use Authorization Code Grant, use this
class GoogleLogin(CustomSocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    # CALLBACK_URL_YOU_SET_ON_GOOGLE
    callback_url = 'http://127.0.0.1:8000/accounts/google/login/callback/'
    client_class = OAuth2Client


def google_view(request):

    # This View just gets the code and prints on the terminal.

    code = request.GET.get('code')
    print(f"The code is : {code}")
    print("go to the browser to make a post request")

    
    """
    # Alternatively, you can send a post request from directly.

    response = requests.post('http://127.0.0.1:8000/dj/google', data={'code': code})
    print("status: " + response.status_code)
    print(response.json()['access_token'])
    """

    return redirect('google-rest')

# https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=http://127.0.0.1:8000/accounts/google/login/callback/&prompt=consent&response_type=code&client_id=878674025478-e8s4rf34md8h4n7qobb6mog43nfhfb7r.apps.googleusercontent.com&scope=openid%20email%20profile&access_type=offline

