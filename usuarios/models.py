from django.db import models

class Usuario(models.Model):

    nome = models.CharField(max_length = 50, null = False, blank = False)
    email = models.EmailField(max_length=30, null=False, blank=False)
    senha = models.CharField(max_length=25, null=False, blank=False)


    def __str__(self):
        return f'Usuario  [nome = {self.nome}]'