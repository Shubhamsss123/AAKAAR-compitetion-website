from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.

class TaskZero(models.Model):
    crid = models.CharField(max_length=10)
    username = models.CharField(max_length = 200)
    colgName = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    mobileNo = models.CharField(max_length=10)
    dept = models.CharField(max_length = 200)
    whatsappNo = models.CharField(max_length = 10)
    pincode = models.CharField(max_length = 6)
    address = models.CharField(max_length = 200)
    

    def __str__(self):
        return (
            f"{self.username} | "
            f"{self.crid} "
            # f"{self.colgName} "
            # f"{self.state} "
            # f"{self.mobileNo} "
            # f"{self.whatsappNo} "
            # f"{self.address} "
            # f"{self.pincode} "
            # f"{self.dept}"
        )

class TaskOne(models.Model):
    crid = models.CharField(max_length=10)
    username = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = "aakarapp/images")
    marks = models.CharField(max_length = 200, default="")
    
    

    def __str__(self):
        return (
            f"{self.username} "
            f"{self.crid} "
        )


