from django.db import models
from django.utils import timezone
# Create your models here.
class Portfolio (models.Model):
    name = models.CharField(max_length=200) 
    type = models.CharField(max_length=100)
    description = models.TextField()
    image_portfolio = models.ImageField(upload_to='images/' ,blank=True,  null= True)
    dateCreated = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

class myPodcard (models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField(max_length=500)
    category = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
