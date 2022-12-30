from django.db import models

# Create your models here.
class Livros(models.Model):
    titulo = models.CharField("Titulo",max_length=50)
    autor = models.CharField("Autor",max_length=50)
    anoPublicacao = models.IntegerField("Ano de Publicação")
    numeroPaginas = models.IntegerField("Número de Páginas")
    isbn = models.IntegerField("ISBN")
    editora = models.CharField("Editora",max_length=50)
    emailEditora = models.EmailField("E-mail da Editora")

    def __str__(self) -> str:
        return self.titulo