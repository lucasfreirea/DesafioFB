from django.db import models

# Create your models here.

class Establishment(models.Model):

    class Meta:

        db_table = 'establishment'

    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.title
