from django.urls import path
import django_forms_auth.views  as form_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView


urlpatterns = [
    
    path('', form_views.index, name= 'index'),
    
    path('register', form_views.register, name= 'register'),
    path('login', form_views.login_view, name= 'login'),
    path('logout', form_views.logout_view, name= 'logout'),
    path('changepassword', form_views.changepassword, name= 'changepassword'),
    path ('password-reset', PasswordResetView.as_view(), name='password-reset')

]
