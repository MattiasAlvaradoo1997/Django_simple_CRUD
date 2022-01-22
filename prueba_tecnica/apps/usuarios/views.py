from django.shortcuts import redirect, render
from .models import Usuario
from django.contrib import messages

# Create your views here.

def home(request):

    
    queryset = request.GET.get("id")
    if(queryset):
        usuario = Usuario.objects.filter(id=queryset)
    else:
        usuario = Usuario.objects.all()
    return render(request, "gestionUsuarios.html", {"usuarios":usuario})

def registrarUsuario(request):

    nombre   = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    email    = request.POST['txtEmail']
    fecha    = request.POST['txtFecha']

    if Usuario.objects.filter(email=email).exists():
        messages.success(request, 'El E-mail ya existe')

    else:
        usuario = Usuario.objects.create(nombre=nombre, apellido=apellido, email=email, fecha=fecha)
        messages.success(request, '¡Usuario registrado!')
    return redirect('/')

def eliminarUsuario(request, id):

    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    messages.success(request, '¡Usuario eliminado!')

    return redirect('/')

def edicionUsuario(request, id):

    usuario = Usuario.objects.get(id=id)
    return render(request, "edicionUsuario.html", {"usuario":usuario})

def editarUsuario(request):
    
    id       = request.POST['txtID']
    nombre   = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    email    = request.POST['txtEmail']
    fecha    = request.POST['txtFecha']

    usuario = Usuario.objects.get(id=id)

    usuario.nombre=nombre
    usuario.apellido = apellido
    usuario.email = email
    usuario.fecha = fecha

    usuario.save()
    messages.success(request, '¡Usuario modificado!')

    return redirect('/')
