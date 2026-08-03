from django.db import models
from django.contrib.auth.models import User


class Prediction(models.Model):

    name = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)

    fingerprint = models.ImageField(upload_to='fingerprints/')
    predicted_group = models.CharField(max_length=5)
    confidence = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return self.name