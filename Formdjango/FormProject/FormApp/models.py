from sqlite3 import Date
from django.db import models
import datetime


# Create your models here.

class Applicant(models.Model):
    name = models.CharField('Applicant name', max_length=200, unique=True)
    address = models.CharField(max_length=200)
    zip_code = models.CharField('Zip code', max_length=15)
    phone = models.CharField('Contact Phone', max_length=11)
    DateOfBirth = models.DateField(default=Date.today)
    web = models.URLField('Website address', blank=True)
    Male="Male"
    Female='Female'
    cho=((Male,"Male"), (Female, "Female"))
    gender = models.CharField('Gender', max_length=6, choices=cho, default=Male)
    email_address = models.EmailField('Email address', blank=True)
    paid = models.BooleanField(default=False)
    RegDate=models.DateTimeField(default=datetime.datetime.now)

    

    def __str__(self):
        return self.name
