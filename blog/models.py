from django.db import models
from model_utils.models import TimeStampedModel


class Post(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    description = models.TextField()

    def __str__(self):
        return self.title
