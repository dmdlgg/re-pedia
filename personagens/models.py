from django.db import models

class Personagens(models.Model):
    nome = models.CharField()
    idade = models.IntegerField()
    historia = models.CharField()
    aparicoes_jogos = models.CharField()
    aparicoes_filmes_series = models.CharField()
    adaptacoes = models.CharField()
    sexo = models.CharField(default='')
    imagem = models.ImageField(upload_to='personagens/', blank=True, null=True)
    


