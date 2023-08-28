from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=150)
    header_image=models.ImageField(null=True,blank=True,upload_to="images/")
    # author=models.ForeignKey(User,on_delete=models.CASCADE)
    desc=models.TextField()
    # image = models.ImageField(upload_to='blog_images/')
    
    # def __str__(self):
    #     return self.title + ' | ' + str(self.author)
    
    