from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db.models import Q
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes, action
from .serializers import *
from rest_framework import status
from newApi.utils import *


@api_view(["POST"])
@permission_classes([AllowAny])
# Create your views here.
def signup(request):
    username = request.data.get("username")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    phone_number = request.data.get("phone_number")
    password = request.data.get("Password")
    
    
    new_user = IMUser.objects.create(
        username = username,
        first_name = first_name,
        last_name = last_name,
        phone_number = phone_number
    )
    
    new_user.set_password(password)
    new_user.save()
    # new_user.generate_auth_token()
    serializers = AuthSerializer(new_user, many = False)
    return Response ({"message": "Account successfully creatd", "result": serializers.data})
    
    
@api_view(["POST"])
@permission_classes([AllowAny])
def user_login(request):
    #1. Receive inputs/data from client and validate inputs
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"detail": "My friend behave yourself and send me username and password"}, status.HTTP_400_BAD_REQUEST)
        #2. Check user existence

    try:
        user = IMUser.objects.get(username=username)
        #3. User authentications
        auth_user = authenticate(username=username, password=password)
        if auth_user:
            if not user.is_active:
                return Response({"detail": "Your account is inactive. Please contact support."}, status.HTTP_403_FORBIDDEN)
            user.temporal_login_fail = 0
            user.save()
                #4. Login user
            login(request, user)
            serializer = AuthSerializer(user, many=False)
            return Response({"result": serializer.data }, status.HTTP_200_OK)

        else:
            user.temporal_login_fail += 1
            user.save()
            return Response({"detail": "Invalid credentials"}, status.HTTP_400_BAD_REQUEST)

    except IMUser.DoesNotExist:
        return Response({"detail": "Username does not exist"}, status.HTTP_400_BAD_REQUEST)
    
class UserViewSet(viewsets.ModelViewSet):
    
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password', None)
        player_id = request.data.get('player_id', None)
        
        user = authenticate(email=email, password=password)
        login(request, user)

        
class ForgotPasswordAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        #1. receive the username (email)
        username = request.data.get("username")
        if not username:
            return generate_400_response("Please provide valid username")
       
            
        #2. check if the user exist
        try:
            user = IMUser.objects.get(username=username)
            
            #3. send OTP code
            otp_code = generate_unique_code()
            user.unique_code =  otp_code
            user.save()
            
            #4. respond to tthe user
            return Response({"detail": "Please check your email for an OTP Code"}, status.HTTP_200_OK)
            
        except IMUser.DoesNotExist:
            return generate_400_response("Username does not exist")
        
        
class ResetPasswordAPIView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        username = request.data.get("username")
        unique_code = request.data.get("unique_code")
        password = request.data.get("password")
        
        if not (username and unique_code and password):
            return generate_400_response("Please provide the correct username")
        
        try:
            user = IMUser.objects.get(username = username) 
            if not user.unique_code == unique_code:
                return generate_400_response("try again")
            else:
                user.set_password(password)
                user.unique_code = ""
                user.save()
                user.is_blocked = True
                user.is_active = True
                user.temporal_login_fail = 0
                user.permanent_login_fail = 0
                  
                user = AuthSerializer(user, context = {"request": request})
                return Response({"message":"password reset successfully"}, status.HTTP_200_OK)
        except IMUser.DoesNotExist:
            return generate_400_response("username does not exist")
        
class CurrentUserProfileAPIView(APIView):
    def get(self, request):
        print(request.user)
        return Response(UserSerializer(request.user).data)
    
class ChangePasswordAPIView(APIView):
    def post(self, request):
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        user_obj = request.user
        user = UserSerializer(user_obj).data
        print(user)
        
        if not (old_password and new_password):
            return generate_400_response("field cannot be blank")
        auth_user = authenticate(username=user['username'], password=old_password)
        if auth_user:
            auth_user.set_password(new_password)
            auth_user.save()
            return Response({"message":"password changed successfully"}, status.HTTP_200_OK)
        return generate_400_response('authentication failed')
        
        

