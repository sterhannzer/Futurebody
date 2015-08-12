from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    barcode = models.IntegerField()

    def __unicode__(self):
        return self.name + self.surname + " " + str(self.barcode)
