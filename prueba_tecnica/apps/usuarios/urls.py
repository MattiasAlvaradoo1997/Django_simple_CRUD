from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarUsuario/', views.registrarUsuario),
    path('eliminarUsuario/<id>', views.eliminarUsuario),
    path('edicionUsuario/<id>', views.edicionUsuario),
    path('editarUsuario/', views.editarUsuario),
]