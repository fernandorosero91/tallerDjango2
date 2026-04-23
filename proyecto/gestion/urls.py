from django.urls import path
from . import views

urlpatterns = [

    # ─────────────────────────────────────────
    # FBV — Vistas por Función
    # ─────────────────────────────────────────

    # Autores FBV
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/crear/', views.crear_autor, name='crear_autor'),
    path('autores/editar/<int:pk>/', views.editar_autor, name='editar_autor'),
    path('autores/eliminar/<int:pk>/', views.eliminar_autor, name='eliminar_autor'),

    # Libros FBV
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
    path('libros/editar/<int:pk>/', views.editar_libro, name='editar_libro'),
    path('libros/eliminar/<int:pk>/', views.eliminar_libro, name='eliminar_libro'),

    # ─────────────────────────────────────────
    # CBV — Vistas Genéricas Basadas en Clases
    # ─────────────────────────────────────────

    # Autores CBV
    path('cbv/autores/', views.AutorListView.as_view(), name='cbv_lista_autores'),
    path('cbv/autores/crear/', views.AutorCreateView.as_view(), name='cbv_crear_autor'),
    path('cbv/autores/editar/<int:pk>/', views.AutorUpdateView.as_view(), name='cbv_editar_autor'),
    path('cbv/autores/eliminar/<int:pk>/', views.AutorDeleteView.as_view(), name='cbv_eliminar_autor'),

    # Libros CBV
    path('cbv/libros/', views.LibroListView.as_view(), name='cbv_lista_libros'),
    path('cbv/libros/crear/', views.LibroCreateView.as_view(), name='cbv_crear_libro'),
    path('cbv/libros/editar/<int:pk>/', views.LibroUpdateView.as_view(), name='cbv_editar_libro'),
    path('cbv/libros/eliminar/<int:pk>/', views.LibroDeleteView.as_view(), name='cbv_eliminar_libro'),
]
