from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


# Create your models here.

G_CHOICES = (
    ("1", "Male"),
    ("2", "Female"),
    ("3", "Third Gender"),)

D_CHOICES = (
    ("1", "----------"),
    ("2", "Cardiology"),
    ("3", "Neurology"),
    ("4", "Orthopedics"),
    ("5", "Dermatology"),
    ("6", "Nephronology"),
    ("7", "Gynacologist"),
)


class appointmentmodel(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=G_CHOICES)
    age = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=12)
    email_id = models.EmailField(max_length=250)
    country = CountryField()
    department = models.CharField(max_length=20, choices=D_CHOICES)
    reports = models.ImageField(upload_to="reports")


# -----------------UPDATING CONTENT DYNAMICALLY------------------#


class main_content(models.Model):
    description = models.CharField(max_length=2000)
    backgroundimage = models.ImageField(upload_to="dynamic_pics")
