from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True)

    def __str__(self):
        return str(self.name)
