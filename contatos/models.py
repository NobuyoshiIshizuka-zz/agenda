from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    data = models.DateTimeField(default=timezone.now())
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m')

    def __str__(self):
        return self.nome

