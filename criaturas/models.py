from django.db import models

class Criaturas(models.Model):
    nome = models.CharField()
    jogo = models.CharField()
    descricao = models.CharField()
    imagem = models.ImageField(upload_to='criaturas/', blank=True, null=True)
