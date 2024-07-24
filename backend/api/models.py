# models.py
from django.contrib.auth.models import User
from django.db import models

class Player(models.Model):
    STARCRAFT_RANKS = [
        ('bronze', 'Bronze'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
        ('platinum', 'Platinum'),
        ('diamond', 'Diamond'),
        ('master', 'Master'),
        ('grandmaster', 'Grandmaster'),
        ('n/a', 'N/A')
    ]
    STARCRAFT_RACES = [
        ('terran', 'Terran'),
        ('zerg', 'Zerg'),
        ('protoss', 'Protoss'),
        ('n/a', 'N/A')
    ]
    LEAGUE_RANKS = [
        ('iron', 'Iron'),
        ('bronze', 'Bronze'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
        ('platinum', 'Platinum'),
        ('emerald', 'Emerald'),
        ('diamond', 'Diamond'),
        ('master', 'Master'),
        ('grandmaster', 'Grandmaster'),
        ('challenger', 'Challenger'),
        ('n/a', 'N/A')
    ]
    LEAGUE_ROLE = [
        ('top', 'Top'),
        ('jungle', 'Jungle'),
        ('mid', 'Mid'),
        ('adc', 'ADC'),
        ('support', 'Support'),
        ('fill', 'Fill'),
        ('n/a', 'N/A')
    ]
    LEAGUE_SECONDARY_ROLE = [
        ('top', 'Top'),
        ('jungle', 'Jungle'),
        ('mid', 'Mid'),
        ('adc', 'ADC'),
        ('support', 'Support'),
        ('fill', 'Fill'),
        ('n/a', 'N/A')
    ]
    DOODAD_HUNT_LEVEL = [
        ('new', 'New'),
        ('experienced', 'Experienced'),
        ('expert', 'Expert')
    ]

    CS2_ELO_CHOICES = [(i, str(i)) for i in range(0, 30001, 1000)]

    name = models.CharField(max_length=100)
    starcraftrank = models.CharField(max_length=100, choices=STARCRAFT_RANKS, default='n/a')
    starcraftrace = models.CharField(max_length=100, choices=STARCRAFT_RACES, default='n/a')
    leaguerank = models.CharField(max_length=100, choices=LEAGUE_RANKS, default='n/a')
    leaguerole = models.CharField(max_length=100, choices=LEAGUE_ROLE, default='n/a')
    leaguesecondaryrole = models.CharField(max_length=100, choices=LEAGUE_SECONDARY_ROLE, default='n/a')
    cs2elo = models.IntegerField(choices=CS2_ELO_CHOICES, default=0)
    profimage = models.CharField(max_length=255, default='default_image_url')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='players')
    doodadlevel = models.CharField(choices=DOODAD_HUNT_LEVEL, default='new')
    
    def __str__(self):
        return self.name


EVENTS_GAMES = [
    ('Starcraft', 'Starcraft'),
    ('League of Legends', 'League of Legends'),
    ('Counterstrike 2', 'Counterstrike 2'),
    ('Multigame', 'Multigame'),
    ('Other', 'Other')
]

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    game = models.CharField(max_length=100)
    teamsize = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')
    players = models.ManyToManyField(User, related_name='signed_events', blank=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    event = models.ForeignKey(Event, related_name='teams', on_delete=models.CASCADE)
    players = models.ManyToManyField(User, related_name='teams', blank=True)

    class Meta:
        unique_together = ('name', 'event')

    def __str__(self):
        return self.name