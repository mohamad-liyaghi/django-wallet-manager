from django.db import models
from account.models import User
# Create your models here.
class Transaction(models.Model):
    class Choices(models.TextChoices):
        add = "+","add"
        cost = "-","cost"
    title = models.CharField(max_length=120)
    description = models.TextField()
    action = models.CharField(max_length=1,choices=Choices.choices)
    mount = models.PositiveSmallIntegerField(default=0,blank=True,null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
