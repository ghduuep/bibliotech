from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from biblioteca.views import LivroViewSet, UsuarioViewSet, EmprestimoViewSet

router = routers.DefaultRouter()
router.register('livros', LivroViewSet, basename='Livros')
router.register('usuarios', UsuarioViewSet, basename='Usuarios')
router.register('emprestimos', EmprestimoViewSet, basename='Emprestimos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
