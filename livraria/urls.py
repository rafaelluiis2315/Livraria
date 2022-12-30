from django.urls import path
from .views import livro_list, livro_new, livro_edit, livro_remove

urlpatterns = [
    path('', livro_list, name='listar_livros'),
    path('livro_new/', livro_new, name='livro_new'),
    path('livro_edit/<int:livro_id>', livro_edit, name='livro_edit'),
    path('livro_remove/<int:livro_id>', livro_remove, name='livro_remove')
]
