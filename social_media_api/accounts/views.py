# accounts/views.py
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer , UserSerializer
from django.contrib.auth import get_user_model

class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data['token']
        return Response({'token': token})


CustomUser = get_user_model()  # Reference your custom user model

class UserListView(generics.GenericAPIView):
    """
    View to list all users in the system.
    Only accessible to authenticated users.
    """
    queryset = CustomUser.objects.all()  # Query all users
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Return a list of all users.
        """
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
