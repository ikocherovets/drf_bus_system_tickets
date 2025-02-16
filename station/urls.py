from django.urls import path
from .views import BusDetail, BusList

app_name = "station"

urlpatterns  = [
    path("buses/", BusList.as_view(), name="bus_list"),
    path("buses/<int:pk>", BusDetail.as_view(), name="bus_detail"),
]