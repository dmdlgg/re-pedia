from django.db import models

class Armas(models.Model):
    nome = models.CharField()
    jogo = models.CharField()
    imagem = models.ImageField(upload_to='armas/', blank=True, null=True)