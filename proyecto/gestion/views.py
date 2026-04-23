from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Libro
from .forms import AutorForm, LibroForm

# CRUD Autores
def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'gestion/lista_autores.html', {'autores': autores})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'gestion/form.html', {
        'form': form,
        'titulo': 'Crear Autor',
        'cancelar_url': '/autores/',
    })

def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'gestion/form.html', {
        'form': form,
        'titulo': 'Editar Autor',
        'cancelar_url': '/autores/',
    })

def eliminar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('lista_autores')
    return render(request, 'gestion/confirm_delete.html', {
        'tipo': 'Autor',
        'objeto': autor.nombre,
        'cancelar_url': '/autores/',
    })

# CRUD Libros
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'gestion/lista_libros.html', {'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'gestion/form.html', {
        'form': form,
        'titulo': 'Crear Libro',
        'cancelar_url': '/libros/',
    })

def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'gestion/form.html', {
        'form': form,
        'titulo': 'Editar Libro',
        'cancelar_url': '/libros/',
    })

def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'gestion/confirm_delete.html', {
        'tipo': 'Libro',
        'objeto': libro.titulo,
        'cancelar_url': '/libros/',
    })
