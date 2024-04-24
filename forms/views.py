from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer

class UserFormSubmissionView(CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({"message": "Form data submitted successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
