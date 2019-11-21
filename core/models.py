from django.db import models


class Cliente (models.Model):
    nome = models.CharField(max_length= 100)
    email = models.CharField(max_length= 50)
    endereco =models.CharField(max_length= 100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'clientes'
