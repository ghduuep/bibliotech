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

class Usuario(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nome

class Emprestimo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.livro} foi pegado por {self.usuario}'

