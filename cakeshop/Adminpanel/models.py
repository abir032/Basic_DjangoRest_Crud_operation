from statistics import mode
from django.db import models

# Create your models here.

class adminpanel(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length= 100)
    admin_pass = models.CharField(max_length=200)
    admin_email = models.CharField(max_length=100)
    def _str_(self):
        return self.admin_id
class customer(models.Model):
    cus_id = models.AutoField(primary_key=True)
    cus_name = models.CharField(max_length= 100)
    cus_pass = models.CharField(max_length=200)
    cus_email = models.CharField(max_length=100)