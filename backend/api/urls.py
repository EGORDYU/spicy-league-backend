from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib import admin
from rest_framework_simplejwt.views import TokenRefreshView
from .views import PlayerList, PlayerDetail, CustomTokenObtainPairView, UserRegistrationView
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, TeamViewSet
from rest_framework import routers
from .views import get_csrf_token


router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'teams', TeamViewSet, basename='team')

urlpatterns = [
    path('', include(router.urls)),
    path('players/', PlayerList.as_view(), name='player-list'),
    path('csrf-token/', get_csrf_token),
    path('players/<int:pk>/', PlayerDetail.as_view(), name='player-detail'),
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)