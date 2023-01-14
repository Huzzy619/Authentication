from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username','password1', 'password2']  #Add other fields as your project requires


class LoginForm(AuthenticationForm):
    class Meta:
        model  = get_user_model()
        fields = ['username', 'password']