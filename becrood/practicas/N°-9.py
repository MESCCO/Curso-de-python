#Programa para calcular potencias a partir de números ingresados por el usuario
def pedir_num():
    b = int(input("Ingrese el número base: "))
    e= int(input("Ingrese el exponente: "))
    return b, e
def calcular_potencia(b, e):
    return b ** e
# Obtener datos del usuario
numero_base, numero_exponente = pedir_num()
# Calcular y mostrar los cuadrados del 1 al 10
print("\nPotencias del 1 al 10 al cuadrado:\n")
for numero in range(1, 11):
    resultado = calcular_potencia(numero, 2)
    print(f"{numero} elevado al cuadrado es {resultado}")