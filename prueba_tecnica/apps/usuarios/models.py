from django.db import models
import uuid
# Create your models here.

class Usuario(models.Model):

    id       = models.AutoField(primary_key=True)
    nombre   = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email    = models.EmailField(unique=True)
    fecha    = models.DateField()

    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.nombre, self.apellido)