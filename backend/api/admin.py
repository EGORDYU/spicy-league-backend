# backend/api/admin.py
from django.contrib import admin
from .models import Player
from .models import Event

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name','starcraftrank', 'starcraftrace', 'leaguerank', 'leaguerole', 'leaguesecondaryrole', 'cs2elo', 'profimage')
    search_fields = ('name','starcraftrank', 'starcraftrace', 'leaguerank', 'leaguerole', 'leaguesecondaryrole', 'cs2elo', 'profimage')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'game', 'teamsize', 'created_by')
    search_fields = ('name', 'game')
    list_filter = ('date', 'game')
    ordering = ('date',)