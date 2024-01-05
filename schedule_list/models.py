from django.db import models

class Schedule(models.Model):
    host_name = models.CharField(max_length=200)
    guest_name = models.CharField(max_length=200)
    date = models.DateTimeField()
    memo = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class 