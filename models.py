from django.db import models

class Contact(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
