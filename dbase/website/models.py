from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Profile(models.Model):
    SEX = [
        ("M","Male"),
        ("F","Female")
    ]
    BIRTH_YEAR_CHOICES = range(1970,2018)

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    birth_year = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)


    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    
