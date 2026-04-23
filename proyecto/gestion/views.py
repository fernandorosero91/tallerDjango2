from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Autor, Libro
from .forms import AutorForm, LibroForm

# ─────────────────────────────────────────
# VISTAS POR FUNCIÓN (Function-Based Views)
# ─────────────────────────────────────────

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'gestion/fbv/lista_autores.html', {'autores': autores})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'gestion/fbv/form.html', {
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
    return render(request, 'gestion/fbv/form.html', {
        'form': form,
        'titulo': 'Editar Autor',
        'cancelar_url': '/autores/',
    })

def eliminar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('lista_autores')
    return render(request, 'gestion/fbv/confirm_delete.html', {
        'tipo': 'Autor',
        'objeto': autor.nombre,
        'cancelar_url': '/autores/',
    })

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'gestion/fbv/lista_libros.html', {'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'gestion/fbv/form.html', {
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
    return render(request, 'gestion/fbv/form.html', {
        'form': form,
        'titulo': 'Editar Libro',
        'cancelar_url': '/libros/',
    })

def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'gestion/fbv/confirm_delete.html', {
        'tipo': 'Libro',
        'objeto': libro.titulo,
        'cancelar_url': '/libros/',
    })


# ─────────────────────────────────────────
# VISTAS GENÉRICAS (Class-Based Views)
# ─────────────────────────────────────────

class AutorListView(ListView):
    model = Autor
    template_name = 'gestion/cbv/lista_autores.html'
    context_object_name = 'autores'

class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'gestion/cbv/form.html'
    success_url = reverse_lazy('cbv_lista_autores')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['titulo'] = 'Crear Autor'
        ctx['cancelar_url'] = '/cbv/autores/'
        return ctx

class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'gestion/cbv/form.html'
    success_url = reverse_lazy('cbv_lista_autores')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['titulo'] = 'Editar Autor'
        ctx['cancelar_url'] = '/cbv/autores/'
        return ctx

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'gestion/cbv/confirm_delete.html'
    success_url = reverse_lazy('cbv_lista_autores')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['tipo'] = 'Autor'
        ctx['objeto'] = self.object.nombre
        ctx['cancelar_url'] = '/cbv/autores/'
        return ctx

class LibroListView(ListView):
    model = Libro
    template_name = 'gestion/cbv/lista_libros.html'
    context_object_name = 'libros'

class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/cbv/form.html'
    success_url = reverse_lazy('cbv_lista_libros')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['titulo'] = 'Crear Libro'
        ctx['cancelar_url'] = '/cbv/libros/'
        return ctx

class LibroUpdateView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/cbv/form.html'
    success_url = reverse_lazy('cbv_lista_libros')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['titulo'] = 'Editar Libro'
        ctx['cancelar_url'] = '/cbv/libros/'
        return ctx

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'gestion/cbv/confirm_delete.html'
    success_url = reverse_lazy('cbv_lista_libros')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['tipo'] = 'Libro'
        ctx['objeto'] = self.object.titulo
        ctx['cancelar_url'] = '/cbv/libros/'
        return ctx
