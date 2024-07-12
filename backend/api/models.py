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

    CS2_ELO_CHOICES = [(i, str(i)) for i in range(0, 30001, 1000)]

    name = models.CharField(max_length=100)
    starcraftrank = models.CharField(max_length=100, choices=STARCRAFT_RANKS, default='n/a')
    starcraftrace = models.CharField(max_length=100, choices=STARCRAFT_RACES, default='n/a')
    leaguerank = models.CharField(max_length=100, choices=LEAGUE_RANKS, default='n/a')
    leaguerole = models.CharField(max_length=100, choices=LEAGUE_ROLE, default='n/a')
    leaguesecondaryrole = models.CharField(max_length=100, choices=LEAGUE_SECONDARY_ROLE, default='n/a')
    cs2elo = models.IntegerField(choices=CS2_ELO_CHOICES, default=0)
    profimage = models.CharField(max_length=255, default='https://t4.ftcdn.net/jpg/00/64/67/27/360_F_64672736_U5kpdGs9keUll8CRQ3p3YaEv2M6qkVY5.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='players', default=1)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    game = models.CharField(max_length=100)
    teamsize = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    players = models.ManyToManyField(User, related_name='signed_events', blank=True)

    def __str__(self):
        return self.name