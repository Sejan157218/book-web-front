
from rest_framework import serializers
from .models import *




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
            model = Category
            fields= '__all__' 
            depth=1



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
            model = Author
            fields= '__all__' 
            depth=1


class BookSerializer(serializers.ModelSerializer):
    selling_Price = serializers.SerializerMethodField()
    class Meta:
            model = Book
            fields= '__all__' 
            depth=1

    def get_selling_Price(self,obj):
        return obj.selling_Price
       


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
            model = Order
            fields= '__all__' 
