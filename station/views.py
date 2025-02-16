from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, mixins
from station.models import Bus
from .serializers import BusSerializer

class BusList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

    def get(self, request, *args, **kwargs) -> Response:
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs) -> Response:
        return self.create(request, *args, **kwargs)
        
        

class BusDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset =  Bus.objects.all()
    serializer_class = BusSerializer

    def get(self, request, *args, **kwargs) -> Bus:
        return self.retrieve(self, request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs) -> Response:
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs) -> Response:
        return self.destroy(request, *args, **kwargs)

