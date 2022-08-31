from django.db import models

class Employe(models.Model):
    name=models.CharField(max_length=20)
    department=models.CharField(max_length=50)
    salary=models.PositiveIntegerField()
    experience=models.PositiveIntegerField()

    def __str__(self):
        return self.name
# Create your models here.
