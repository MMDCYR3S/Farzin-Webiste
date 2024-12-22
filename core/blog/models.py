from django.db import models
from django.contrib.auth.models import User

# Post model
class Post(models.Model):
    photographer = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog/", default="blog/default.jpg")
    title = models.CharField(max_length=250)
    content = models.TextField()
    category = models.ManyToManyField("Category")
    #tag
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
