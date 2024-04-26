from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Contacts(models.model):
    phone_num = models.IntegerField()
    adress = models.TextField(max_length=200)
    address_link = models.URLField()
    email = models.EmailField()
    
    