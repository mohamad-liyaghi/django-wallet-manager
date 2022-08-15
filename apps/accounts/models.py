from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    fund = models.PositiveSmallIntegerField(default=0,blank=True,null=True)

