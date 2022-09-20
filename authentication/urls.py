
from django.urls import path
from .views import *

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('signup/',SignUp,name='signup'),
    path('login/',Login,name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('phoneotp/',PhoneOTP.as_view(),name='phoneotp'),
    path('phoneotp/<str:email>/',PhoneOTP.as_view(),name='phoneotp')
]