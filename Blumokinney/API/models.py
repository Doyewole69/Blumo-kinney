from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True,blank=False,null=False)
    phone_number = models.IntegerField(blank=False, unique=True, null=False)

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','first_name','last_name']

    def __str__(self):
        return self.email



        

