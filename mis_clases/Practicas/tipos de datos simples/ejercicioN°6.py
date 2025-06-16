"""Escribir un programa que lea un entero positivo,n
, introducido por el usuario y después muestre en pantalla la suma 
de todos los enteros desde 1 hasta n 
. La suma de los 
n primeros enteros positivos puede ser calculada de la siguiente forma:(n)(n+1)/2
"""
#primera forma con formula
n= int(input("Ingrese un entero positivo : "))
suma=(n*(n+1)/2)
print(f"La suma de los n primeros enteros positivos es {suma}")

#segunda forma
n= int(input("Ingrese un entero positivo : "))
contador1=0
suma1=0
while contador1<=n:
    suma1+=contador1
    contador1+=1
print(f"La suma de los n primeros enteros positivos es {suma1}")

#tercera forma 
n= int(input("Ingrese un entero positivo : "))
contador2=0
for i in range(n+1):
    contador2+=i
print(f"La suma de los n primeros numeros positivo es {contador2}")
    

