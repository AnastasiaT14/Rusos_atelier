from rest_framework import generics
from .models import AboutUs
from .serializers import AboutUsSerializer


class AboutUsAdd(generics.CreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class AboutUsUpdate(generics.UpdateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class AboutUsDelete(generics.DestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer