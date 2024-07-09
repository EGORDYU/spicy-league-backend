from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib import admin
from rest_framework_simplejwt.views import TokenRefreshView
from .views import PlayerList, PlayerDetail, CustomTokenObtainPairView

urlpatterns = [
    path('players/', PlayerList.as_view(), name='player-list'),
    path('players/<int:pk>/', PlayerDetail.as_view(), name='player-detail'),
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
