from rest_framework import viewsets
from biblioteca.models import Livro, Emprestimo
from biblioteca.serializers import LivroSerializer, EmprestimoSerializer
from django.utils import timezone
from django.db import models

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

    def get_queryset(self):
        horario_atual = timezone.now()
        return Emprestimo.objects.filter(models.Q(data_devolucao__isnull=True) | models.Q(data_devolucao__gt=horario_atual))
    



