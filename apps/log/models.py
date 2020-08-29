from django.db import models

from apps.user.models import User


class Log(models.Model):
    username = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    log_time = models.DateTimeField()
    data = models.TextField()
