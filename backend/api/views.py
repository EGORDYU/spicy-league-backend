from rest_framework import generics, permissions
from .models import Player
from .serializers import PlayerSerializer, CustomTokenObtainPairSerializer, UserRegistrationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import Event
from .serializers import EventSerializer
from rest_framework.decorators import action

class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Player.objects.filter(user=self.request.user)
        return Player.objects.all()

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated(), IsOwner()]

    def get_serializer_context(self):
        return {'request': self.request}

class VerifyTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'Token is valid', 'user': request.user.username})


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        player_data = {
            'name': request.data.get('username'),
            'starcraftrank': request.data.get('starcraftrank', 'n/a'),
            'starcraftrace': request.data.get('starcraftrace', 'n/a'),
            'leaguerank': request.data.get('leaguerank', 'n/a'),
            'leaguerole': request.data.get('leaguerole', 'n/a'),
            'leaguesecondaryrole': request.data.get('leaguesecondaryrole', 'n/a'),
            'cs2elo': request.data.get('cs2elo', 0),
            'profimage': request.data.get('profimage', 'default_image_url'),
            'user': user.id
        }

        player_serializer = PlayerSerializer(data=player_data)
        player_serializer.is_valid(raise_exception=True)
        player_serializer.save()

        return Response(user_serializer.data, status=status.HTTP_201_CREATED)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action == 'signup':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def signup(self, request, pk=None):
        event = self.get_object()
        event.players.add(request.user)
        return Response({'status': 'signed up'}, status=status.HTTP_200_OK)