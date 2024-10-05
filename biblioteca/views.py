from rest_framework import viewsets
from biblioteca.models import Livro
from biblioteca.serializers import LivroSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


