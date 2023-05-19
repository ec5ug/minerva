from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, null=True, choices=[("student", "student"), ("school_admin", "school_admin")])
    date_of_update = models.DateField(null=True)
    age = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(123)], null=True)
    edu_lvl = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=14, null=True)
    county = models.CharField(max_length=30, null=True)
    school = models.CharField(max_length=50, null=True)
    gpa = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True)
    classes = models.CharField(max_length=100, null=True)
    intended_major = models.CharField(max_length=20, null=True)
    interests = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.user) + " " + str(self.role)