from django.db import models

class Jogos(models.Model):
    nome = models.CharField(blank=False, null=False)
    data_lancamento = models.CharField(blank=False, null=False)
    sinopse = models.CharField(blank=False, null=False)
    imagem = models.ImageField(upload_to='jogos/', blank=True, null=True)
