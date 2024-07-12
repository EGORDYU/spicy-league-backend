from django.contrib import admin
from .models import Player, Event, Team

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

class PlayerInline(admin.TabularInline):
    model = Team.players.through
    extra = 1

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = [PlayerInline]
    list_display = ('name', 'event')
    search_fields = ('name',)
    list_filter = ('event',)

# Remove these lines to avoid double registration
# admin.site.register(Player)
# admin.site.register(Event, EventAdmin)
# admin.site.register(Team, TeamAdmin)
