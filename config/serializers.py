from rest_framework import serializers
from .models import AboutUs,Contacts



class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['title', 'description']

class ContactSerializer(serializer.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
    
