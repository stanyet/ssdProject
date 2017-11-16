from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = models.CharField(max_length=1, default='M',choices=GENDER_CHOICES)
    profileFilled  = models.IntegerField(default=0)
    bdate = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    def profile_status(self):
        if self.profileFilled == 0:
            return False
        else:
            return True
