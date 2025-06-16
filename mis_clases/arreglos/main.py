import arreglos
numero = int(input("ingrese el numero de elmentos"))
arreglo1= arreglos.leer_arreglo(numero)
arreglos.mostar_arreglo(arreglo1)
elemento = int(input("ingrese numero de elementos para b"))
encontro=arreglos.busca_elemento(arreglo1,elemento)
if(encontro):
    print("el elemento esta en el arreglo")
else:
    print("el elemento no esta en el arreglo")
