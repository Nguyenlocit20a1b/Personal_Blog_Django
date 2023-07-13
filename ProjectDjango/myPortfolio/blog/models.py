from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post (models.Model):
    title = models.CharField(max_length=200)
    blog_img = models.ImageField(upload_to='images/' ,blank=True,  null= True)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User , on_delete=models.CASCADE )
    def __str__(self):
        return self.title
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #  phương thức reverse() được sử dụng để tạo ra URL từ tên định danh của một view. 
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
