from django.db import models


class User(models.Model):
    username = models.TextField(max_length=50, unique=True, null=False, blank=False)


class Finger(models.Model):
    username = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    finger_id = models.IntegerField()
    finger_data = models.TextField()
