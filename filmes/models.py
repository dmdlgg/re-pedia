from django.db import models

class Filmes(models.Model):
    nome = models.CharField(blank=False, null=False)
    data_lancamento = models.CharField(blank=False, null=False)
    duracao = models.CharField(blank=False, null=False)
    sinopse = models.TextField(blank=False, null=False, default='...')
    imagem = models.ImageField(upload_to='filmes/', blank=True, null=True)
