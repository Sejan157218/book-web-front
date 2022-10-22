from pickle import TRUE
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser 



class CustomUserManager(BaseUserManager):
    def create_user(self,username,email,password=None,phone=None,phoneOTP=None,**extra_fields):
     
        if not username:
            raise ValueError("the given username is not valid")
        
        # if len(password)<8:
        #     raise ValueError("password must be 8 character")


        email=self.normalize_email(email)

        user=self.model(
            username=username,
            email=email,
            phone=phone,
            phoneOTP=phoneOTP,
            **extra_fields
        )

        user.set_password(password)
        user.save()

        return user;

    def create_superuser(self,username,email,password,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError ("Superuser has to have is_staff bbeing True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError ("Superuser has to have is_superuser being True")

        return self.create_user(email=email,username=username,password=password,**extra_fields)

class User(AbstractUser):
    email=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    phone=models.CharField(max_length=20,blank=True,null=True)
    phoneOTP=models.IntegerField(blank=True,null=True)



    objects=CustomUserManager()
    USERNAME_FIELD="username"
    REQUIRED_FIELDS=["email"]

    def __str__(self):
        return self.username