from django.db import models


class Photo(models.Model):
    artist = models.CharField(max_length=200)
    photo = models.ImageField()

    def __str__(self):
        return "%s - %s" % (self.artist, self.photo)