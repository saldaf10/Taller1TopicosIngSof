from django.db import models
from django.utils.timezone import now
from datetime import datetime

class Equipment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    ticket_number = models.AutoField(primary_key=True) 
    call_time = models.DateTimeField()
    priority = models.CharField(max_length=50)
    discussion = models.TextField()
    state = models.CharField(max_length=50)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    contact_name = models.CharField(max_length=100)
    Support_name = models.CharField(max_length=20, default="", null=True, blank=True) 
    first_follow_up = models.CharField(max_length=500, default="", null=True, blank=True)
    second_follow_up = models.CharField(max_length=500, default="", null=True, blank=True)
    third_follow_up = models.CharField(max_length=500, default="", null=True, blank=True)
    id_unico = models.IntegerField(unique=True, default=1) 
    time_finish = models.DateTimeField(default=datetime(1, 1, 1, 0, 0, 0))
