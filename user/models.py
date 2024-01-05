from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length=200, default='1234')
    mail = models.CharField(max_length =200)
    is_active = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)