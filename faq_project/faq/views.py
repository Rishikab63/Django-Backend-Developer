from django.shortcuts import render
from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class FAQDetailView(generics.RetrieveAPIView):  # Add this
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
