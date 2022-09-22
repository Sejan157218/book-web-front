
from django.urls import path
from .views import *

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('all-book/', AllBook, name="all-book"),
    path('category/', CategoryObject, name="category"),
    path('author/', AuthorObject, name="author"),
    path('category/<str:pk>/', BookByCategory, name="category-by-book"),
    path('author/<str:pk>/', BookByAuthor, name="author-by-book"),
    path('search/<str:pk>/', SearchData, name="search"),
    path('details/<str:pk>/',DetailsData,name='details'),
    path('order/',OrderView.as_view(),name='order'),
    path('order/<str:pk>/',OrderView.as_view(),name='order')
]
