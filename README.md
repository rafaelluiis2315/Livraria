# Livraria
Projeto contem um CRUD com Django, para gerenciamen de livros, com criação de formularios reativos com o Django e django-bootstrap5


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
Página Inicial (url:"")
![livro_list](https://user-images.githubusercontent.com/98782405/210030236-20cb77d3-3132-471d-99f4-36e6415829e4.png)
Página de cadastro (url:"livro_new/")
![add_livros](https://user-images.githubusercontent.com/98782405/210030285-c253b67d-e1f2-44bd-9174-7b80a8d41d4c.png)
Página de edição (url:"livro_edit/id_do_livro")
![Edite_livro](https://user-images.githubusercontent.com/98782405/210030373-1b4177a6-26b5-4692-82c4-f44cca33e8b0.png)
Página de remoção (url:"livro_remove/id_do_livro")
![delete_livros](https://user-images.githubusercontent.com/98782405/210030403-033d12d5-83e4-4938-be89-60f73f531343.png)
