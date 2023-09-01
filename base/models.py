from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField( max_length=254)
    link = models.CharField(max_length=50 , null = True )
    
    def __str__(self) -> str:
        return self.name

class Advocate(models.Model):
    username = models.CharField(max_length= 20)
    bio = models.TextField(max_length=100 , null=True , blank= True)
    company = models.ForeignKey(Company,on_delete= models.SET_NULL,null=True)
    
    def __str__(self) -> str:
        return self.username
    
