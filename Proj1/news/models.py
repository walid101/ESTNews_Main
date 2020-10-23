from django.db import models

class News(models.Model):
    headlines = models.TextField()
    date = models.DateField()
    summary = models.TextField()
    title = models.fields.CharField(max_length=1000, default = " ")