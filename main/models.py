from __future__ import unicode_literals

from django.db import models

# Create your models here.
class IK(models.Model):
    titre = models.CharField(max_length = 255)
    numero = models.IntegerField()
    texte = models.CharField(max_length = 1000)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    fichier = models.FileField(default = None, upload_to="uploads/")
    miniature = models.ImageField(default = None, upload_to="uploads/miniatures/")

    def __unicode__(self):
        return self.titre

class Article(models.Model):
    titre = models.CharField(max_length = 10000)
    auteur = models.CharField(max_length = 255)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    fichier = models.FileField(default = None, upload_to="uploads/articles/")
    validation = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.titre
