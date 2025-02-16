from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from station.models import Bus
from rest_framework.views import APIView
from .serializers import BusSerializer

class BusList(APIView):
    def get(self, request) -> Response:
        buses = Bus.objects.all()
        serializer = BusSerializer(buses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request) -> Response:
        serializer = BusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class BusDetail(APIView):
    def get_object(self, pk: int) -> Bus:
        return get_object_or_404(Bus, pk=pk)
    
    def get(self, request, pk: int) -> Response:
        serializer = BusSerializer(self.get_object(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk: int) -> Response:
        serializer = BusSerializer(self.get_object(pk=pk), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk: int) -> Response:
        self.get_object(pk=pk).delete()

