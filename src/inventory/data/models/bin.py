from django.db import models
from . import Area


class Bin(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
