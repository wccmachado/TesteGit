from django.db import models

# Create your models here.
class teste(models.Model):
    nome=models.CharField(max_length=100)

class teste2(models.Model):
    idade = models.CharField(max_length=100)