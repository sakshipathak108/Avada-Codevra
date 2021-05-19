from django.db import models


class findform(models.Model):
    rqd_skills = models.CharField(max_length=5000)
    eventchosen = models.CharField(max_length=200)
    fname_event = models.CharField(max_length=500)
    lname_event = models.CharField(max_length=500)
    msid_event = models.CharField(max_length=500)

    def __str__(self):
        return self.msid_event
