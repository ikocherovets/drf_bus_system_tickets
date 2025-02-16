from django.urls import path
from .views import bus_detail, bus_list

app_name = "station"

urlpatterns  = [
    path("buses/", bus_list, name="bus_list"),
    path("buses/<int:pk>", bus_detail, name="bus_detail"),
]