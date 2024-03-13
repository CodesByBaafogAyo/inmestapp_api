from rest_framework import serializers
from users.models import *

class AuthSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    auth_token = serializers.CharField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    email = serializers.EmailField()

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    auth_token = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()

class CohortSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    year = serializers.IntegerField()  
    description = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    author = UserSerializer(many = False)  

class CohortMemberSerializer(serializers.Serializer):
    member = UserSerializer(many = False) 
