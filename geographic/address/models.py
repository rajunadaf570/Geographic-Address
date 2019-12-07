#python imports.
import uuid

#django imports.
from django.db import models

#project level imports.
from libs.models import TimeStampedModel


class LatLongAddress(TimeStampedModel):
    """
    LatLongAddress model represents the address and 
    latlong into database.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.TextField(blank=False, default='')
    latitude = models.CharField(max_length=60, blank=False)
    longitude = models.CharField(max_length=64, blank=False)
