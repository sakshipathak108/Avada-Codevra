from django.db import models


class findform(models.Model):
    rqd_skills = models.CharField(max_length=5000)
    eventchosen = models.CharField(max_length=200)
    fname_event = models.CharField(max_length=500)
    regno = models.CharField(max_length=100, default='')
    msid_event = models.CharField(max_length=500)
    your_skills = models.CharField(max_length=5000, default='')

    def __str__(self):
        return self.msid_event
