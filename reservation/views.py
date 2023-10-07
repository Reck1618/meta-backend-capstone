from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookingSerializer, MenuSerializer
from rest_framework import generics, viewsets
from .models import Booking, Menu

# Create your views here.
def home(request):
    return render(request, 'index.html')

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer