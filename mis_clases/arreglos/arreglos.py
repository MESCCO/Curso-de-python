"""Libreria para operaciones con arreglos
-leer arreglo"""
def leer_numero():
    numero=int(input("Ingrese un numero entero: "))
    return numero

def leer_arreglo(numero):
    arreglo=[]
    for i  in range(numero):
        arreglo.append(i)
        return arreglo
    
def mostrar_arreglo(arreglo):
    print("los elementos del arreglo son: ")
    for i in range(len(arreglo)):
     print(arreglo[i],end=" ")
            
def busca_elemento(arreglo,elemento):
    for i in range(len(arreglo)):
        if elemento==arreglo[i]:
            return True
    return False

