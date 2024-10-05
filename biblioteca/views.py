from rest_framework import viewsets
from biblioteca.models import Livro, Usuario, Emprestimo
from biblioteca.serializers import LivroSerializer, UsuarioSerializer, EmprestimoSerializer
from django.utils import timezone

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

    def get_queryset(self):
        horario_atual = timezone.now()
        return Emprestimo.objects.filter(data_devolucao__gt=horario_atual)
    



