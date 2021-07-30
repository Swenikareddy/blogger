from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date

class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')
    '''def save(self,*args,**kwargs):
        self.name=self.name.lower()
        return super(Category,self).save(*args,**kwargs)'''
# Create your models here.
class MyPost(models.Model):
    title=models.CharField(max_length=300)
    header_image=models.ImageField(null=True,blank=True,upload_to='images/')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    pdate=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=255,default='coding')
    likes=models.ManyToManyField(User,related_name='blog_posts')

    #category=models.ForeignKey(Category,max_length=100,on_delete=models.CASCADE,related_name='catego')
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')
        #return reverse('details',args=(str(self.id)))

