

from django.db import models


#import models from another apps



class User_profile(models.Model):

    email = models.EmailField(max_length=255, unique=True, null=True)
    password = models.CharField(max_length=255, unique=True, null=True)