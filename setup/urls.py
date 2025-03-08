from django.contrib import admin # Importa o módulo admin do Django
from django.urls import path, include # Importa as funções path e include

urlpatterns = [ # Define a lista de padrões de URL do projeto
    path('admin/', admin.site.urls), # Mapeia a URL 'admin/' para as URLs do admin do Django
    path('', include('Sin_Quiz.urls')) # Inclui as URLs do app Sin_Quiz na raiz do projeto.
]