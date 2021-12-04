from django.db import models

# Create your models here.
 
class Login(models.Model):  
    lname = models.CharField(max_length=80)  
    lemail = models.EmailField(max_length=100)  
    lpasswd = models.CharField(max_length=30)  
    laddress = models.CharField(max_length=250)  
    class Meta:  
        db_table = "login" 
