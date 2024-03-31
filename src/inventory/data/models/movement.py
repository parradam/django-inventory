from django.utils.timezone import now
from django.db import models
from . import Item, Bin


class Movement(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    bin_from = models.ForeignKey(Bin, related_name="bin_from", on_delete=models.CASCADE)
    bin_to = models.ForeignKey(Bin, related_name="bin_to", on_delete=models.CASCADE)
    completed_at = models.DateTimeField(default=now)
