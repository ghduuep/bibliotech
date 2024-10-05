from django.contrib import admin
from biblioteca.models import Livro

class Livros(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'autor', 'genero',]
    list_display_links = ['titulo',]
    list_per_page = 20
    search_fields = ['titulo', 'autor', 'genero']
    list_filter = ['autor', 'genero']


admin.site.register(Livro, Livros)
