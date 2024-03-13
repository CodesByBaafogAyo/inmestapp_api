from django.urls import path
from .views import *

urlpatterns = [
    path("users/signup/", signup),
    path('users/login/', user_login),
    path('users/forgot_password/', ForgotPasswordAPIView.as_view()),
    path("reset_password/", ResetPasswordAPIView.as_view()),
    path('change_password/', ChangePasswordAPIView.as_view()),
    path('users/me/', CurrentUserProfileAPIView.as_view()),
    
]
