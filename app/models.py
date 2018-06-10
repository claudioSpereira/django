from django.db import models

# Create your models here.
class Client(models.Model):
    cli_name = models.CharField(max_length=50)
    cli_register = models.IntegerField()



class Notifications(models.Model):
    nt_name = models.CharField(max_length=50)
    nt_register = models.IntegerField()