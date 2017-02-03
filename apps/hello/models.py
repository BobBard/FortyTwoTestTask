from django.db import models


class UserData(models.Model):
    username = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.CharField(max_length=100)
    skype = models.CharField(max_length=100)
    birth_date = models.DateField()
    jabber = models.EmailField()
    other_contacts = models.TextField(max_length=300)
