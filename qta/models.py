from django.db import models

# Create your models here.
class Ticket(models.Model):
    ticket_number = models.CharField(max_length=20)
    call_time = models.DateTimeField()
    priority = models.CharField(max_length=20)
    discussion = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    equipment = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=20)
    contact_name = models.CharField(max_length=20)
    first_follow_up = models.CharField(max_length=500)
    second_follow_up = models.CharField(max_length=500)
    third_follow_up = models.CharField(max_length=500)