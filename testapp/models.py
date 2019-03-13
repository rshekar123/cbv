from django.db import models
from django.urls import reverse

# Create your models here.

class shekar(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    salary=models.FloatField()

    def get_absolute_url(self):
        return reverse('list')
