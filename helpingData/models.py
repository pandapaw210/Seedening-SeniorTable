from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    content = models.TextField()


    