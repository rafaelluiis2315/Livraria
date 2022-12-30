# Livraria
Projeto contem um CRUD com Django, para gerenciamen de livros


## Estrutura do Projeto

~~~
    Livraria(repositorio)
    ├── Project
    |   ├── __init__.py
    |   ├── asgi.py
    |   ├── settings.py ("Confiração geral do projeto")
    |   ├── urls.py ("Mapeamento geral de urls do projeto")
    |   └── wsgi.py
    |       
    ├── livraria 
    |   └── migrations ("As migrações do banco ficam guardadas")
    |       ├──  0001_initial.py 
    |       └──  0002_alter_livros_anopublicacao_alter_livros_autor_and_more.py 
    |   └── templates
    |       ├── base.html ("Template base")
    |       ├── livro_delete.html ("Template da pagina de Remoção de livros")
    |       ├── livro_form.html ("Template da pagina de cadastros e remoção de livros ")
    |       └── livro_lista.html ("Template da pagina principal, listagem de livros")
    |   ├── admin.py 
    |   ├── apps.py 
    |   ├── models.py ("Model do banco usado no app")
    |   ├── tests.py
    |   ├── urls.py ("Gerenciamento das urls do app")
    |   └── views.py ("Controler da apliação")
    |    
    └── manage.py ("Gerenciador da aplicação Django ")
~~~


## Como Rodar o Projeto

1. Ter uma venv (ambiente virtual) e ativala.
2. Instalar Bibliotecas 
   1. ~~~ 
        pip install django 
      ~~~
   2. ~~~ 
        pip install django-bootstrap5
      ~~~
3. Ir na raiz do projeto (onde está o "manage.py"), execute os comandos:
    1. ~~~ 
        py manage.py migrate 
        ~~~
   2. ~~~ 
        py manage.py runserver
        ~~~

## Fotos do Projeto
