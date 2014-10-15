from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name
