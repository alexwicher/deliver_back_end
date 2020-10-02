from django.db import models

from user.models import User


class Address(models.Model):
    address = models.CharField(null=False, max_length=64)
    user = models.ForeignKey(User, related_name='address_user', on_delete=models.CASCADE, null=False)
