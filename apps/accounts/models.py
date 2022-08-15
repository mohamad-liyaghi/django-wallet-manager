from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, nick_name, balance, password, **kwargs):

        email = self.normalize_email(email)

        user = self.model(email= email, nick_name= nick_name, balance= balance, is_active=True, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, nick_name, balance, password, **kwargs):
        return  self.create_user(email=email, nick_name=nick_name, balance=balance, password= password,
                                 is_superuser= True, is_staff=True)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=120)
    nick_name = models.CharField(max_length=120)

    balance = models.PositiveSmallIntegerField(default=0, blank=True, null=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects= UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nick_name', 'balance']

    def __str__(self):
        return self.email