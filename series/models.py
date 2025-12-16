from django.db import models

class Series(models.Model):
    nome = models.CharField(blank=False, null=False)
    data_lancamento = models.CharField(blank=False, null=False)
    qtde_eps = models.IntegerField
    sinopse = models.TextField(blank=False, null=False)
    imagem = models.ImageField(upload_to='series/', blank=True, null=True)
