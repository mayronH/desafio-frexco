import random
import string
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    """Custom User with birth date"""
    username = models.CharField(max_length = 50, blank = False, null = False, unique = True)
    birthdate = models.DateField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['birthdate']

    def __str__(self):
        return self.username
    
    def make_password():
        """Generate random password with 8 digits"""
        sample = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.sample(sample, 8))
        
        return password