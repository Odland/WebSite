from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=512)
    article =  models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
