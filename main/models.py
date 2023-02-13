from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=256)
    date = models.PositiveBigIntegerField()
    scope = models.CharField(max_length=50)
    order = models.PositiveIntegerField()
    main_img = models.CharField(max_length=100)
    summary = models.TextField()
    techical_detail = models.TextField(null=True)
    roles = models.TextField(null=True)
    roles_list = models.TextField(null=True)
    challenges = models.TextField(null=True)
    results = models.TextField(null=True)
    show = models.BooleanField()

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
    position = models.CharField(max_length=100, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.alt


