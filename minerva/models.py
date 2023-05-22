from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class Scholarship(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    prize_money = models.FloatField(MinValueValidator(0.01))
    deadline = models.DateTimeField()
    date_of_posting = models.DateTimeField()
    country = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    organization = models.CharField(max_length=100, null=True, blank=True)
    min_age = models.IntegerField(MinValueValidator(1), null=True, blank=True)
    max_age = models.IntegerField(MinValueValidator(1), null=True, blank=True)
    min_grade = models.IntegerField(MinValueValidator(0), null=True, blank=True)
    max_grade = models.IntegerField(MinValueValidator(0), null=True, blank=True)
    min_gpa = models.FloatField(MinValueValidator(0), null=True, blank=True)
    url = models.URLField()