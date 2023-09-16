from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=30, null=False)
    phone = models.TextField(max_length=30, null=True)