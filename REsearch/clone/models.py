from django.urls import reverse
from django.db import models


class SeqFile(models.Model):
    file = models.FileField()
