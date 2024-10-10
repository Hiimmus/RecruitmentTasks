from django.db import models


class Pesel(models.Model):
    number = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.number
