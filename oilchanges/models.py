from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Oilchange(models.Model):
    subject = models.CharField(max_length=200)
    details = models.CharField(max_length=200)
