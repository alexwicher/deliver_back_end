from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phoneNumber = models.CharField(max_length=150, blank=True)
    email = models.EmailField(error_messages={
        'unique': "A user with that e-mail already exists.",
    }, unique=True, max_length=150,

    )

    def __str__(self):
        return self.username
