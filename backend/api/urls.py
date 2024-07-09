# api/urls.py
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('players/', views.PlayerList.as_view(), name='player-list'),
    path('players/<int:id>/', views.PlayerDetail.as_view(), name='player-detail'),
    path('', TemplateView.as_view(template_name='index.html')),
]
