from django.contrib.auth.models import User
from django.db import models


class UserData(models.Model):
    user = models.OneToOneField(User, to_field='id', on_delete=models.CASCADE)
    surname = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    skype = models.CharField(max_length=100)
    birth_date = models.DateField()
    jabber = models.EmailField()
    other_contacts = models.TextField(max_length=300)
