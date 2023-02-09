from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=256)
    date = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name


class Tech(models.Model):
    name = models.CharField(max_length=100)
    project = models.ManyToManyField(Project)

    def __str__(self):
        return self.name
    

class Img(models.Model):
    url = models.CharField(max_length=100)
    alt = models.CharField(max_length=256)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.alt


