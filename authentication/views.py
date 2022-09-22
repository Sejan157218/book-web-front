from symbol import pass_stmt
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import status
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from .models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import json
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import random
# Create your views here.
class index(APIView):
    def get(self, request, format=None):
        data={
                "": "Authentication",
            }
        return Response(data)



@api_view(['POST'])
def SignUp(request):
    if request.method=="POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user=User.objects.get(email=serializer.data["email"])
            login(request,user)
            token_obj,_=Token.objects.get_or_create(user=user)
            data={
                "username": user.username,
                "email": user.email,
                "phone" : user.phone,
                "token":str(token_obj),
               
            }
            return Response({"msg":"Successfully", "payload":data,"status":status.HTTP_201_CREATED})    
        else:
            emessage=serializer.errors
            return Response({'error': emessage}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def Login(request):
    if request.method=="POST":
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            # user=User.objects.get(email=serializer.data.get("email"))
            # login(request,user)
            # print("serializer",serializer.data.get("password"))
            userAuthenticate = authenticate(username=serializer.data.get("email"), password=serializer.data.get("password"))
         
           
            if userAuthenticate:
                
                login(request,userAuthenticate)
               
                token_obj,_=Token.objects.get_or_create(user=userAuthenticate)
             
                data={
                "username": userAuthenticate.username,
                "email": userAuthenticate.email,
                "phone" : userAuthenticate.phone,
                "token":str(token_obj),
               
            }
                return Response({"msg":"Successfully",'payload':data, "status":status.HTTP_201_CREATED}) 
            return Response({"error":"You have entered an invalid username or password"},status=status.HTTP_400_BAD_REQUEST)
            
        # else:
        #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 



class Logout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]   
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        logout(request)
        return Response({"msg":"LogOut successfully"},status=status.HTTP_200_OK)


class PhoneOTP(APIView):
    def get(self,request,email):
        user=User.objects.get(email=email)
      
        return Response({"msg":"Otp Send","OTP":user.phoneOTP,"status":status.HTTP_200_OK})


    def post(self,request):
  
        serializer=ConfirmOTPSerializer(data=request.data)
        if serializer.is_valid():
            user=User.objects.get(email=serializer.data["email"])
          
            if user.phoneOTP==serializer.data["phoneOTP"]:
                print(user.phoneOTP==serializer.data["phoneOTP"])
                user.set_password(serializer.data["password"])
                user.save()
                return Response({"msg":"Password Change Successfully ", "status":status.HTTP_201_CREATED}) 
        return Response({"error":"The OTP entered is incorrect"},status=status.HTTP_401_UNAUTHORIZED)

    def put(self,request):
        serializer=OTPSerializer(data=request.data)
        if serializer.is_valid():
            otp=str(random.randint(1000,9999))
            user=User.objects.filter(email=serializer.data["email"],phone=serializer.data["phone"]).first()
            print(serializer.data["email"],serializer.data["phone"])

            if user:
                user.phoneOTP=otp
                user.save()
                return Response({"msg":"Otp Send"},status=status.HTTP_200_OK)
            # else:
            #     return Response({"error":"You have entered an invalid email or phone"},status=status.HTTP_400_BAD_REQUEST)
        return Response({"error":"You have entered an invalid email or phone"},status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','POST'])
# def Login(request):

#     if request.method=="POST":
#         # print(request.data['email'])
#         # user=User.objects.get(email=request.data['email'])
#         # if user.email==request.data['email'] and user.password==request.data['password']:

#         #    login(request,user)
#         #    return Response({"msg":"Successfully"}, status=status.HTTP_201_CREATED) 
#             # print(user)
#         serializer = LoginSerializer(data=request.data)
#         # print(serializer.is_valid())
#         if serializer.is_valid():
#             user=User.objects.get(email=serializer.data.get("email"))
#             # print("password",serializer.data)
#             login(request,user)
#             return Response({"msg":"Successfully"}, status=status.HTTP_201_CREATED) 
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)    
        # if authenticated_user != None:

        #     if(authenticated_user):
        #         login(request,authenticated_user)
        #         return JsonResponse({"Message":"User is Authenticated. "})   
        #     else:
        #         return JsonResponse({"message":"User is not authenticated. "})
        # else:
        #     return JsonResponse({"Message":"Either User is not registered or password does not match"})
        # if serializer.is_valid(raise_exception=True):
        #     login(request,serializer.data)

    # return Response(serializer.data, status=status.HTTP_201_CREATED)    
        # else:
        #     emessage=serializer.errors
        #     return Response({'error': emessage}, status=status.HTTP_400_BAD_REQUEST)

        # data={
        #         "": "Authentication",
        #     }
        # return Response(data)
            