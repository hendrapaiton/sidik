from django.db import models


class Device(models.Model):
    device_name = models.TextField(max_length=50, unique=True, null=False, blank=False)
    sn = models.TextField(max_length=50, unique=True, null=False, blank=False)
    vc = models.TextField(max_length=50, unique=True, null=False, blank=False)
    ac = models.TextField(max_length=50, unique=True, null=False, blank=False)
    vkey = models.TextField(max_length=50, unique=True, null=False, blank=False)
