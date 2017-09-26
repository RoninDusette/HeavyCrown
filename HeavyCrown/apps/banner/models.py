from django.db import models


class BannerVideo(models.Model):
    video_code = models.CharField(max_length=100)

    def __str__(self):
        return self.video_code
