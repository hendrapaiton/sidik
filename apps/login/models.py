from django.db import models

from apps.user.models import User


class Finger(models.Model):
    username = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    finger_id = models.IntegerField()
    finger_data = models.TextField()
