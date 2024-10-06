from rest_framework import viewsets, serializers
from biblioteca.models import Livro, Emprestimo
from biblioteca.serializers import LivroSerializer, EmprestimoSerializer
from django.utils import timezone
from django.db import models

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def perform_create(self, serializer):
        titulo = serializer.validated_data['titulo']
        autor = serializer.validated_data['autor']
        if Livro.objects.filter(titulo=titulo, autor=autor).exists():
            raise serializers.ValidationError('Titulo ja adicionado a biblioteca!')
        
        serializer.save()


class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

    def get_queryset(self):
        horario_atual = timezone.now()
        return Emprestimo.objects.filter(models.Q(data_devolucao__isnull=True) | models.Q(data_devolucao__gt=horario_atual))

    def perform_create(self, serializer):
        usuario = serializer.validated_data['usuario']
        livro = serializer.validated_data['livro']

        if Emprestimo.objects.filter(usuario=usuario, data_devolucao__isnull=True).exists():
            raise serializers.ValidationError('Este usuario ja possui um emprestimo ativo')
        
        if Emprestimo.objects.filter(livro=livro, data_devolucao__isnull=True).exists():
            raise serializers.ValidationError(f'{livro} esta em um emprestimo ativo')
        
        serializer.save()