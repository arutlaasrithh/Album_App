from django.db import models
import uuid

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
#    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    photo = models.ImageField(upload_to="myimage")

#class Categoty(models.Model):
#    name = models.CharField(max_length=50)
