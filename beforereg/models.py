from django.db import models
from django.contrib.auth.models import User


class register_table(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.CharField(max_length=200)
    skills = models.CharField(max_length=10000)

    def __str__(self):
        return self.user.first_name
