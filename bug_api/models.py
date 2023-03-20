from django.db import models

class Bug(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    year_identified = models.IntegerField()

    def __str__(self):
        return self.name
