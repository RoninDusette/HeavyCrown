from django.db import models


class Quote(models.Model):
    quote = models.CharField(max_length=300)

    def __str__(self):
        return "Quote"
