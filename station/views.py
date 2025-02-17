from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, mixins
from station.models import Bus
from .serializers import BusSerializer

class BusList(
    generics.ListCreateAPIView,
):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
        
        
class BusDetail(
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset =  Bus.objects.all()
    serializer_class = BusSerializer

