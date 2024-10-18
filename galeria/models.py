from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Fotografia(models.Model):

    opcoes_categoria = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALAXIA', 'Galaxia'),
        ('PLANETA', 'Planeta'),
        ('ASTRO', 'Astro')
    ]

    nome = models.CharField(max_length = 100, null = False, blank = False)
    legenda =  models.CharField(max_length=200, null = False, blank = False)
    categoria = models.CharField(max_length=70, choices=opcoes_categoria, default='')
    descricao = models.TextField(null = False, blank = False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True, null=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='usuario'
    )
    

    def __str__(self):
        return f'Fotografia  [nome = {self.nome}]'



