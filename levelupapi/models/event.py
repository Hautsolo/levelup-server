from django.db import models
from .game import Game
from .gamer import Gamer

class Event(models.Model):
    game = models.ForeignKey(Game , on_delete=models.CASCADE, related_name='events')
    description = models.CharField(max_length=50)
    date = models.DateField(max_length=10)
    time = models.TimeField(max_length=15)
    organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE, related_name='event')
    
    