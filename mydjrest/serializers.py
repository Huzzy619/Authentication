from urllib.parse import unquote

from dj_rest_auth.registration.serializers import SocialLoginSerializer


class CustomSocialLoginSerializer(SocialLoginSerializer):

    def validate(self, attrs):
        # update the received code to a proper format. so it doesn't throw error.
        
        attrs['code'] = unquote(attrs.get('code'))

        return super().validate(attrs)
