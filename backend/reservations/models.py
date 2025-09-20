from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chambre(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name
    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.chambre.name} ({self.date})"
