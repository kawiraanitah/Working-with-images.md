from django.db import models

# Create your models here.
class Post(models.Model):
    userId = models.IntegerField(default=1)
    title = models.CharField("Default Title",max_length = 200)
    body = models.TextField(default="Body of post goes here")
    def __str__ (self):
        return self.title
    

