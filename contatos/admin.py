from django.contrib import admin
from .models import Contato, Categoria


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','sobrenome', 'telefone', 'email', 'data', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')  # ADD LINK para editar
    # list_filter = ('nome', 'sobrenome')  # ADD filtro
    list_per_page = 10  # Listar 10 elementos por página
    search_fields = ('nome', 'sobrenome', 'email', 'telefone')
    list_editable = ('telefone', 'mostrar')  # Editando o telefone e a aba mostrar


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
