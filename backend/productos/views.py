from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status

from .models import Productos, Categoria
from .serializer import ProductoSerializer



'''
-----------------------------------------------------------
        METODOS PARA LA CREACIÓN DE LAS CATEGORIAS
-----------------------------------------------------------
'''






# Obtenemos todos los productos
@api_view(['GET'])
def get_productos(request):
    productos = Productos.objects.all()
    serializer = ProductoSerializer(productos,many=True)
    return Response(serializer.data)


# Obtenemos un producto
@api_view(['GET'])
def get_productos(request, nombre):
    producto = Productos.objects.get(nombre=nombre)
    serializer = ProductoSerializer(producto,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def crear_producto(request):
    # Preguntamos si el usuario es admin
    # if request.user.is_staff:
    #     pass
    serialiser = ProductoSerializer(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
        return Response(serialiser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialiser.data, status=status.HTTP_400_BAD_REQUEST)

