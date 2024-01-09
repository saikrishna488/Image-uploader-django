from django.db import models
from django.utils import timezone

class Image(models.Model):
    photo = models.ImageField(upload_to="myimages")
    upload_date = models.DateTimeField(auto_now_add=True)

