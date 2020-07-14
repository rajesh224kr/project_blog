from django.db import models

# Create your models here.
class Images(models.Model):
    Iname       = models.CharField(max_length=20,null=True,blank=True)
    Ilocation   = models.CharField(max_length=20,null=True,blank=True)
    image       = models.FileField(upload_to='media/')