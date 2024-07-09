# backend/api/admin.py
from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name','starcraftrank', 'starcraftrace', 'leaguerank', 'leaguerole', 'leaguesecondaryrole', 'cs2elo', 'profimage')
    search_fields = ('name','starcraftrank', 'starcraftrace', 'leaguerank', 'leaguerole', 'leaguesecondaryrole', 'cs2elo', 'profimage')


    # name = models.CharField(max_length=100)
    # starcraftrank = models.CharField(max_length=100, choices=STARCRAFT_RANKS)
    # starcraftrace = models.CharField(max_length=100, choices=STARCRAFT_RACES)
    # leaguerank = models.CharField(max_length=100, choices=LEAGUE_RANKS)
    # leaguerole = models.CharField(max_length=100, choices=LEAGUE_ROLE)
    # leaguesecondaryrole = models.CharField(max_length=100, choices=LEAGUE_SECONDARY_ROLE)
    # cs2elo = models.IntegerField(choices=CS2_ELO_CHOICES)