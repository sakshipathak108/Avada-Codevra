from django.db import models
from django.contrib.auth.models import User


class findform(models.Model):
    rqd_skills = models.CharField(max_length=5000)
    eventchosen = models.CharField(max_length=200)
    fname_event = models.CharField(max_length=500)
    regno = models.CharField(max_length=100, default='')
    msid_event = models.CharField(max_length=100)
    your_skills = models.CharField(max_length=5000, default='')
    branch = models.CharField(max_length=500, default='')

    def __str__(self):
        return str(self.id)


class friendlist(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    friends = models.ManyToManyField(User, related_name="friends", blank=True)

    def __str__(self):
        return self.user.first_name

    def get_friends_no(self):
        return self.friends.all().count()

    def get_friends(self):
        return self.friends.all()




