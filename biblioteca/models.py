from django.db import models

class Livro(models.Model):

    GENEROS = (
        ('NF', 'NAO_FICCAO'),
        ('F', 'FICCAO'),
    )

    titulo = models.CharField(max_length=100, blank=False)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=2, choices=GENEROS, blank=False, null=False, default='F')

    def __str__(self) -> str:
        return self.titulo
