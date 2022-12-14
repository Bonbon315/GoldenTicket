from django.db import models
from django.conf import settings

# Create your models here.


class PlayDetail(models.Model):
    playid = models.CharField(max_length=50)
    playname = models.CharField(max_length=500)
    genrename = models.CharField(max_length=50)
    playstate = models.CharField(max_length=50)
    playstdate = models.DateField()
    playenddate = models.DateField()
    poster = models.CharField(max_length=80)
    locationname = models.CharField(max_length=500)
    playcast = models.CharField(max_length=500, null=True)
    runtime = models.CharField(max_length=50, null=True)
    age = models.CharField(max_length=50, null=True)
    locationid = models.CharField(max_length=50)
    image1 = models.CharField(max_length=80, null=True)
    image2 = models.CharField(max_length=80, null=True)
    image3 = models.CharField(max_length=80, null=True)
    image4 = models.CharField(max_length=80, null=True)
    ticketprice = models.CharField(max_length=500, null=True)
    summary = models.TextField(null=True)
    guidance = models.CharField(max_length=500, null=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="performance"
    )


class LocationDetail(models.Model):
    locationid = models.CharField(max_length=200)
    locationname = models.CharField(max_length=300)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=200)
    relateurl = models.CharField(max_length=500)
    lat = models.CharField(max_length=200)
    lgt = models.CharField(max_length=200)
