from django.db import models

# Create your models here.
class course(models.Model):
    cid = models.CharField(max_length=100,primary_key=True)
    cn = models.CharField(max_length=100)
    
