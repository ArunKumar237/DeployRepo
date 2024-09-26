from django.db import models
class Article(models.Model):
    title = models.TextField() #which accepts only text data
    content = models.TextField()    