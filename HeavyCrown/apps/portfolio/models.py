from django.db import models
from imagekit.models import ProcessedImageField
from versatileimagefield.fields import VersatileImageField, PPOIField


class Photo(models.Model):
    artist = models.CharField(max_length=200)
    photo = VersatileImageField(upload_to='photos/', ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')

    def __str__(self):
        return "%s - %s" % (self.artist, self.photo)