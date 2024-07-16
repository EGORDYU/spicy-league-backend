# api/serializers.py
from rest_framework import serializers
from .models import Player
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Event, Team



class PlayerSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ['id', 'name', 'starcraftrank', 'starcraftrace', 'leaguerank','leaguerole', 'leaguesecondaryrole', 'cs2elo', 'profimage', 'is_owner', 'user']

    def get_is_owner(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.user == request.user
        return False


class UserSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'players']



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if not username or not password:
            raise serializers.ValidationError('Username and password are required')

        user = authenticate(request=self.context.get('request'), username=username, password=password)
        if user is None:
            raise serializers.ValidationError('Invalid login credentials')

        refresh = self.get_token(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return data

    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token
    
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    

class EventSerializer(serializers.ModelSerializer):
    players = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    players = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'
