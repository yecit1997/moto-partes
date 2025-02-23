from django.db import models


class Productos:
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits = 10 , decimal_places = 2 )
    imagen = models.ImageField(upload_to='productos')
    status = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    

