from django.db import models
from core import models as core_models

class List(core_models.TimeStampedModel):
    name = models.CharField(max_length=80)
    temp = [
        'sdf'
    ]