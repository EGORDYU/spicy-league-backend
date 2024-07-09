from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)
    starcraftrank = models.CharField(max_length=100)
    starcraftrace = models.CharField(max_length=100)

    def __str__(self):
        return self.name