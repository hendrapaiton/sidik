from django.db import models


class User(models.Model):
    username = models.TextField(max_length=50, unique=True, null=False, blank=False)
