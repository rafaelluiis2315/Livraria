from django.shortcuts import render, redirect, get_object_or_404
from .models import Livros
from django.forms import ModelForm

# Create your views here.
class LivroForm(ModelForm):
    class Meta:
        model = Livros
        fields = ['titulo', 'autor', 'anoPublicacao', 'numeroPaginas', 'isbn', 'editora', 'emailEditora']

def livro_list(request, template_name='livro_lista.html'):
    livros = Livros.objects.all()
    return render(request, template_name, {'livros': livros})

def livro_new(request, template_name='livro_form.html'):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_livros')
    
    return render(request, template_name, {'form': form, 'titulo':"Cadastro de Livros"})

def livro_edit(request, livro_id, template_name='livro_form.html'):
    livro = get_object_or_404(Livros, pk=livro_id)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            livro = form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, template_name, {'form': form, 'titulo':"Editar Livro"})

def livro_remove(request, livro_id):
    livro = Livros.objects.get(pk=livro_id)
    
    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros')
    return render(request, 'livro_delete.html', {'livro': livro})