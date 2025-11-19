from django.db import models
import django.utils.timezone as timezone
# Create your models here.

class Students(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    enrollment_date = models.DateField(default=timezone.now)
    age = models.IntegerField()