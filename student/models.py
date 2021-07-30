from django.db import models
from django.contrib.auth.models import User, auth


# Create your models here.
class Admin(models.Model):
    Name=models.CharField(max_length=20)
    DOB=models.CharField(max_length=30)
    Phone_Number=models.CharField(max_length=30)
   

class StudentDetails(models.Model):
    Name_of_The_Student=models.CharField(max_length=20)
    DOB=models.CharField(max_length=30)
    Phone_Number=models.CharField(max_length=30)
   


class register_table(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    phone_number = models.CharField(max_length=12)

    def _str_(self):
        return self.user.username

    

    





