from django.db import models


class Application(models.Model):

    name = models.CharField(max_length=100)
    outid = models.CharField(max_length=200)
    keyapi = models.CharField(max_length=200)

    def __str__(self):
        return self.name
