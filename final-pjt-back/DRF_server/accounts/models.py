from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
