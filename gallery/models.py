from django.db import models

# Create your models here.
class Picture(models.Model):
    name            = models.CharField(max_length=255)
    image           = models.ImageField()
    description     = models.TextField()
    pub_date        = models.DateTimeField(auto_now_add=True)