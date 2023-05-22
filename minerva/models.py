from django.db import models
from django.contrib.auth.models import User
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

class Error_Report(models.Model):
    sender = models.OneToOneField(User, on_delete=models.CASCADE, related_name='sent_error_reports')
    sender_message = models.CharField(max_length=250)
    error_type = models.CharField(max_length=250)
    receiver = models.OneToOneField(User, on_delete=models.CASCADE, related_name='received_error_reports', null=True, blank=True)
    receiver_message = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=10, choices=[("pending", "Pending"), ("reviewed", "Reviewed")])
