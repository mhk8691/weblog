from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images/User/")
