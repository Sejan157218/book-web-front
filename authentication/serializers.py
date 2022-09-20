from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import User
from django.contrib.auth import authenticate
import random


# UserModel = get_user_model()



class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)
    # email = serializers.CharField(write_only=True)


    # def create(self, validated_data):

    #     user = UserModel.objects.create_user(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         password=validated_data['password'],
          
    #     )

    #     return user

    class Meta:
        model = User
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "email","password", "phone")




    def validate(self, data):
        user=User.objects.filter(email=data["email"])
        if user.exists():
            raise serializers.ValidationError({"error":"Email already exits.Try another one"})
        if len(data["password"])<8:
            raise serializers.ValidationError({"error":"password length must be 8"})
        return data


    def create(self, validated_data):
        user =User.objects.create(username=validated_data["username"],email=validated_data["email"],phone=validated_data["phone"]) 
        user.set_password(validated_data["password"])  
        user.save()     
        return user





class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        # exclude=['username',"phone","phoneOTP"]

        # extra_kwargs = {'password': {'write_only': True}}
    # def validate(self, data):

    #     # user=User.objects.filter(email=data["email"]) & User.objects.filter(password=data["password"])
    #     # user=User.objects.filter(email=data["email"])
    #     # user=User.objects.filter(password=data["password"])
    #     user = authenticate(username=data["email"], password=data["password"])
    #     if user == None:
    #         raise serializers.ValidationError({"error":"You have entered an invalid username or password"})
  
    #     return user
        
class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'phone')

class ConfirmOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','password', 'phoneOTP')
    # def validate(self, data):
    #     # user=User.objects.filter(email=data['email'],phone=data['phone']) 
    #     user=User.objects.filter(email=data['email']) & User.objects.filter(phone=data['phone'])
    #     if not user:
    #         raise serializers.ValidationError({"error":"You have entered an invalid email or phone"})
    #     return data


    # def update(self, instance, validated_data):
    #     otp=str(random.randint(1000,9999))
    #     instance.phoneOTP=validated_data["phone"]
        
    #     # user=User.objects.filter(email=validated_data["email"]) & User.objects.filter(password=validated_data["phone"])
    #     # user.phoneOTP=otp
    #     print("user")
    #     # user.save()
    #     instance.save()
    #     return instance;