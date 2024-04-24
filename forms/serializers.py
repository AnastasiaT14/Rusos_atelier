from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)
    number = serializers.CharField(max_length=20)
    email = serializers.EmailField()
