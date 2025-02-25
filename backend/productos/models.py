from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre


class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits = 10 , decimal_places = 2 )
    imagen = models.ImageField(upload_to='productos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    

