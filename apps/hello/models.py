from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    jabber = models.EmailField()
    other_contacts = models.TextField(max_length=300)

