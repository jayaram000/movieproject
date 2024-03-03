from django.db import models
# Create your models here.

class Movie(models.Model):
    Name= models. CharField(max_length=20)
    desc = models.CharField(max_length=250)
    year=models. IntegerField()
    img=models.FileField(upload_to="movies/img",null=True,blank=True)
    def __str__(self):
        return self.Name