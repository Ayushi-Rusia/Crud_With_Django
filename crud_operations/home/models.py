from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Person(User):
    contact=models.IntegerField()
    address=models.CharField(max_length=10)
    def __str___(self)-> str:
       return Person.username
