# accounts/serializers.py
# accounts/serializers.py
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # To handle passwords securely

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email', 'bio', 'profile_picture')

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        Token.objects.create(user=user)  # Create a token for the new user
        return user
