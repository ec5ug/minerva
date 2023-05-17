from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, default="student", choices=[("student", "student"), ("school_admin", "school_admin")])
    filled_form = models.BooleanField(default=False)
    date_of_update = models.DateField(null=True)
    age = models.PositiveIntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(123)])
    edu_lvl = models.CharField(null=True, max_length=20)
    state = models.CharField(null=True, max_length=14)
    county = models.CharField(null=True, max_length=30)
    school = models.CharField(null=True, max_length=50)
    gpa = models.FloatField(null=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    classes = models.CharField(max_length=100)
    intended_major = models.CharField(max_length=20)
    interests = models.CharField(max_length=100)