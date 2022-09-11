

from django.http import Http404
from api.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *
from django.contrib.postgres.search import SearchVector,SearchQuery
from django.db.models import Q
# Create your views here.

class index(APIView):
    def get(self, request, format=None):
        data={
                "": "index",
            }
        return Response(data)

@api_view(['GET'])
def CategoryObject(request):
    if request.method=='GET':
        category=Category.objects.all()
        serializer=CategorySerializer(category,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def AuthorObject(request):
    if request.method=='GET':
        category=Author.objects.all()
        serializer=AuthorSerializer(category,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def AllBook(request):
    if request.method=='GET':
        data=Book.objects.all();
        serializer=BookSerializer(data,many=True)
        # serializer.is_valid()
        # serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def BookByCategory(request,pk):
    if request.method=='GET':
        dataAll=Book.objects.all()
        data=dataAll.filter(category__title=pk)
        serializer=BookSerializer(data,many=True)
        return Response(serializer.data)



@api_view(['GET'])
def BookByAuthor(request,pk):
    if request.method=='GET':
        dataAll=Book.objects.all()
        data=dataAll.filter(author__name=pk)
        serializer=BookSerializer(data,many=True)
        return Response(serializer.data)
   



@api_view(['GET'])
def SearchData(request,pk):
        search = Book.objects.annotate(search=SearchVector('category__title', 'author__name','title')).filter(Q(search=pk) | Q(search__icontains=pk)).distinct()
        serializer= BookSerializer(search,many=True)
        return Response(serializer.data)



@api_view(['GET'])
def DetailsData(request,pk):
        data=Book.objects.get(id=pk)
        serializer= BookSerializer(data)
        return Response(serializer.data)