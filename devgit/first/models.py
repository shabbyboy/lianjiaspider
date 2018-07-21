from django.db import models

# Create your models here.
class music(models.Model):
    name = models.TextField(default="that's girl")
    singer = models.TextField(default="shabbyboy")
    lastMotifydate = models.DateField(auto_now=True)
    createdate = models.DateField(auto_now_add=True)

    class meta:
        db_table = "music"
